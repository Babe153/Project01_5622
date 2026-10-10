"""Project01: classify AD/NC using the 90 AAL grey-matter volumes.

Lab 2 structure: load data -> fixed train/test split -> SVM fit/predict/score.
Project01 specifies 40 training subjects and 10 test subjects. All fitting,
including scaling and the optional training-only CV estimate, uses training data.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import sklearn
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

BASE_DIR = Path(__file__).resolve().parent
FEATURE_COLUMNS = [f"ROI_{i}_mm3" for i in range(1, 91)]
TRAIN_IDS = [f"Data_{i:02d}" for i in range(40)]
TEST_IDS = [f"Data_{i:02d}" for i in range(40, 50)]
LABEL_TO_NUMBER = {"NC": 0, "AD": 1}
NUMBER_TO_LABEL = {0: "NC", 1: "AD"}


def normalize_subject(value: str) -> str:
    """Labels have spaces and .nii suffixes; volume tables use plain Data_XX."""
    name = str(value).strip()
    name = re.sub(r"\.nii(?:\.gz)?$", "", name, flags=re.IGNORECASE)
    if re.fullmatch(r"Data_\d{2}", name) is None:
        raise ValueError(f"Invalid subject ID: {value!r}")
    return name


def load_feature_table(path: Path, expected_ids: list[str]) -> pd.DataFrame:
    """Keep ONLY ROI_1..90 as features, in numerical ROI order."""
    table = pd.read_csv(path, encoding="utf-8-sig")
    table.columns = table.columns.str.strip()
    expected_columns = ["FileName", *FEATURE_COLUMNS]
    if len(table.columns) != 91 or set(table.columns) != set(expected_columns):
        raise ValueError(f"{path}: expected FileName plus ROI_1_mm3..ROI_90_mm3.")
    table["FileName"] = table["FileName"].map(normalize_subject)
    if table["FileName"].duplicated().any():
        raise ValueError(f"{path}: duplicate subject IDs.")
    if set(table["FileName"]) != set(expected_ids):
        raise ValueError(f"{path}: subject IDs do not match the Project01 split.")
    table = table.set_index("FileName").loc[expected_ids, FEATURE_COLUMNS]
    table = table.apply(pd.to_numeric, errors="raise")
    values = table.to_numpy(dtype=float)
    if not np.isfinite(values).all() or (values < 0).any():
        raise ValueError(f"{path}: ROI volumes must be finite and non-negative.")
    return table


def load_labels_for(path: Path, subject_ids: list[str]) -> np.ndarray:
    """Join by New Name, never by row position or Original Name."""
    labels = pd.read_csv(path, encoding="utf-8-sig", dtype=str)
    labels.columns = labels.columns.str.strip()
    if not {"New Name", "Label"}.issubset(labels.columns):
        raise ValueError("Label CSV must contain New Name and Label columns.")
    labels["subject_id"] = labels["New Name"].map(normalize_subject)
    if labels["subject_id"].duplicated().any():
        raise ValueError("Label CSV contains duplicate subject IDs.")
    labels = labels.set_index("subject_id")
    missing = set(subject_ids) - set(labels.index)
    if missing:
        raise ValueError(f"Missing labels for {sorted(missing)}.")
    selected = labels.loc[subject_ids, "Label"].str.strip().str.upper()
    if not selected.isin(LABEL_TO_NUMBER).all():
        raise ValueError("Requested labels must be AD or NC.")
    return selected.map(LABEL_TO_NUMBER).to_numpy(dtype=int)


def build_model() -> Pipeline:
    # Same SVM API as Lab 2. These fixed baseline settings are an implementation
    # choice, not parameters mandated by the teacher or tuned on test accuracy.
    return Pipeline([
        ("scaler", StandardScaler()),
        ("svm", svm.SVC(kernel="rbf", C=1.0, gamma="scale")),
    ])


def fit_model(model: Pipeline, x_train: np.ndarray, y_train: np.ndarray):
    """Estimate training-only CV accuracy, then refit on all 40 subjects."""
    if x_train.shape != (40, 90) or set(np.unique(y_train)) != {0, 1}:
        raise ValueError("Training requires a 40x90 matrix with both AD and NC.")
    if np.bincount(y_train, minlength=2).min() < 5:
        raise ValueError("Five-fold stratified CV needs at least five of each class.")
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=73)
    # Pipeline is passed INTO cross_val_score: each fold fits its own scaler.
    cv_scores = cross_val_score(
        model, x_train, y_train, cv=cv, scoring="accuracy", error_score="raise"
    )
    model.fit(x_train, y_train)
    return cv_scores


def save_predictions(model: Pipeline, x_test: np.ndarray, test_ids: list[str],
                     output_dir: Path) -> pd.DataFrame:
    """Predict and persist the report table before using any test labels."""
    if x_test.shape != (10, 90) or test_ids != TEST_IDS:
        raise ValueError("Test input must be Data_40..49 with 90 ROI features.")
    output_dir.mkdir(parents=True, exist_ok=True)
    predicted = model.predict(x_test)
    predictions = pd.DataFrame({
        "FileName": [f"{s}.nii" for s in test_ids],
        "Prediction": [NUMBER_TO_LABEL[int(n)] for n in predicted],
    })
    predictions.to_csv(output_dir / "test_predictions.csv", index=False)
    # Signed distance is a decision score, NOT a probability; AD is positive.
    pd.DataFrame({
        "FileName": predictions["FileName"],
        "AD_decision_score": model.decision_function(x_test),
    }).to_csv(output_dir / "test_decision_scores.csv", index=False)
    return predictions


def save_training_record(model: Pipeline, x_train: np.ndarray, y_train: np.ndarray,
                         cv_scores: np.ndarray, input_paths: dict[str, Path],
                         output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    record = {
        "method": "StandardScaler + SVC (fixed baseline; no hyperparameter search)",
        "kernel": "rbf", "C": 1.0, "gamma": "scale",
        "train_subject_ids": TRAIN_IDS, "test_subject_ids": TEST_IDS,
        "feature_columns": FEATURE_COLUMNS, "feature_units": "mm3",
        "label_encoding": LABEL_TO_NUMBER,
        "training_class_counts": {NUMBER_TO_LABEL[i]: int((y_train == i).sum()) for i in [0, 1]},
        "training_accuracy": float(accuracy_score(y_train, model.predict(x_train))),
        "training_cv": {
            "method": "5-fold StratifiedKFold", "shuffle": True, "random_state": 73,
            "fold_accuracy": cv_scores.tolist(),
            "mean_accuracy": float(cv_scores.mean()),
            "std_accuracy": float(cv_scores.std(ddof=0)),
        },
        "scaler_fitted_subject_count": int(model.named_steps["scaler"].n_samples_seen_),
        "scaler_mean_mm3": model.named_steps["scaler"].mean_.tolist(),
        "scaler_scale_mm3": model.named_steps["scaler"].scale_.tolist(),
        "test_labels_used_for_fitting_or_parameter_selection": False,
        "software_versions": {"numpy": np.__version__, "pandas": pd.__version__, "scikit-learn": sklearn.__version__},
        "input_sha256": {key: hashlib.sha256(path.read_bytes()).hexdigest() for key, path in input_paths.items()},
        "limitations": "Only 40 training and 10 test subjects; fixed baseline; Data_44 retains the previously accepted BET quality limitations.",
    }
    (output_dir / "training_record.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    joblib.dump({"pipeline": model, "feature_columns": FEATURE_COLUMNS,
                 "label_encoding": LABEL_TO_NUMBER}, output_dir / "svm_model.joblib")
    return record


def evaluate_predictions(predictions: pd.DataFrame, labels_path: Path,
                         output_dir: Path) -> dict:
    """Optional final evaluation only; this function never changes the model."""
    y_test = load_labels_for(labels_path, TEST_IDS)
    predicted = predictions["Prediction"].map(LABEL_TO_NUMBER).to_numpy(dtype=int)
    matrix = confusion_matrix(y_test, predicted, labels=[0, 1])
    tn, fp, fn, tp = matrix.ravel()
    report = classification_report(
        y_test, predicted, labels=[0, 1], target_names=["NC", "AD"],
        output_dict=True, zero_division=0,
    )
    metrics = {
        "test_subjects": 10, "accuracy": float(accuracy_score(y_test, predicted)),
        "correct_predictions": int((y_test == predicted).sum()),
        "sensitivity_AD": float(tp / (tp + fn)),
        "specificity_NC": float(tn / (tn + fp)),
        "confusion_matrix_order": ["NC", "AD"],
        "confusion_matrix_rows_true_columns_predicted": matrix.tolist(),
        "classification_report": report,
        "evaluation_only_no_model_updates": True,
    }
    (output_dir / "test_metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    checked = predictions.copy()
    checked["TrueLabel"] = [NUMBER_TO_LABEL[int(n)] for n in y_test]
    checked["Correct"] = y_test == predicted
    checked.to_csv(output_dir / "test_evaluation.csv", index=False)
    import matplotlib.pyplot as plt
    from sklearn.metrics import ConfusionMatrixDisplay
    fig, ax = plt.subplots(figsize=(5, 4.5))
    ConfusionMatrixDisplay(matrix, display_labels=["NC", "AD"]).plot(
        ax=ax, colorbar=False, cmap="Blues", values_format="d"
    )
    ax.set_title("Project01 SVM - test set (n=10)")
    fig.tight_layout()
    fig.savefig(output_dir / "test_confusion_matrix.png", dpi=180)
    plt.close(fig)
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train", type=Path, default=BASE_DIR / "data/AAL_statistics_volumn_train.csv")
    parser.add_argument("--test", type=Path, default=BASE_DIR / "data/AAL_statistics_volumn_test.csv")
    parser.add_argument("--labels", type=Path, default=BASE_DIR / "data/data_labels.csv")
    parser.add_argument("--output-dir", type=Path, default=BASE_DIR / "results")
    parser.add_argument("--evaluate", action="store_true", help="Compare saved predictions with test labels AFTER fitting/predicting.")
    args = parser.parse_args()
    train = load_feature_table(args.train, TRAIN_IDS)
    test = load_feature_table(args.test, TEST_IDS)
    x_train, x_test = train.to_numpy(dtype=float), test.to_numpy(dtype=float)
    y_train = load_labels_for(args.labels, train.index.tolist())
    model = build_model()
    cv_scores = fit_model(model, x_train, y_train)
    predictions = save_predictions(model, x_test, test.index.tolist(), args.output_dir)
    record = save_training_record(model, x_train, y_train, cv_scores,
                                  {"train": args.train, "test": args.test, "labels": args.labels}, args.output_dir)
    print(f"Train: {x_train.shape}; Test: {x_test.shape}; NC=0, AD=1")
    print(f"Training-only 5-fold CV accuracy: {cv_scores.mean():.1%} (std {cv_scores.std():.1%})")
    print(f"Training accuracy: {record['training_accuracy']:.1%} (not test performance)")
    print(predictions.to_string(index=False))
    if args.evaluate:
        metrics = evaluate_predictions(predictions, args.labels, args.output_dir)
        print(f"Test accuracy: {metrics['accuracy']:.1%} ({metrics['correct_predictions']}/10)")
        print(f"AD sensitivity: {metrics['sensitivity_AD']:.1%}; NC specificity: {metrics['specificity_NC']:.1%}")
    print(f"Results saved to: {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
