# Running the Project01 SVM

[English](RUNNING_GUIDE.md) · [中文版](README_运行说明.md)

Predict AD/NC using grey-matter volumes from AAL regions 1–90. Run this stage locally in Windows/VSCode; FSL and a VM connection are not required.

## Files

- `Project01_SVM.ipynb`: executed notebook with English explanations; training, prediction, and final evaluation are implemented.
- `project01_svm.py`: CLI implementation of the same model and shared loading/output helpers.
- `data/`: volumes for 40 training and 10 test subjects, plus a copy of the supplied labels.
- `requirements.txt`: pinned Python dependencies.
- `results/`: actual predictions, metrics, confusion matrix, and saved model. Rerunning updates this directory.

## Run in VSCode

1. Open the entire repository folder in VSCode.
2. Create a Python environment in its terminal (Python 3.12 recommended):

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use `python -m venv .venv` if another supported Python is installed. Install the VSCode Python/Jupyter extensions and select `.venv` as the notebook kernel. The CLI commands invoke that interpreter directly, without an activation script.

3. Open `Project01_SVM.ipynb` and run all cells in order. `EVALUATE_TEST=True` compares the supplied test labels only after fitting and saving predictions.

Fit and export predictions:

```powershell
.\.venv\Scripts\python.exe project01_svm.py
```

Fit, predict, and perform final evaluation:

```powershell
.\.venv\Scripts\python.exe project01_svm.py --evaluate
```

Use `--train`, `--test`, `--labels`, or `--output-dir` for alternative paths. Defaults are relative to the script directory, so the script can locate its data even when launched from another working directory.

## Correspondence with Lab 2 and Project01

| Lab 2 step | Project01 implementation |
| --- | --- |
| Import APIs and Load PIMA | Import `sklearn.svm`; read volume tables; join AD/NC labels by `New Name` |
| `train_test_split` | Use the prescribed Data_00–39 / Data_40–49 split |
| SVM TODO | Fit `svm.SVC` inside a pipeline that first applies `StandardScaler` |
| Output accuracy | Report training fit accuracy, training-only five-fold CV, and final test accuracy separately |

Project01 specifies a fixed 40/10 split and 90 volume features and suggests feature standardization across training samples. The Lab 2 training TODO did not provide completed model code. RBF, C=1, gamma='scale', and five-fold CV are implementation choices, not instructor-specified optimal settings. CV estimates this fixed baseline's performance within the training set; it is not a hyperparameter search.

The project PDF's example table starts with Data_30, while its text and prescribed split identify Data_40–49 as the test set. The code follows the explicit split and predicts these 10 subjects.

## Data handling

1. Normalize whitespace and `.nii` suffixes in the label table's `New Name`, then join by subject ID rather than CSV row position.
2. Use only `ROI_1_mm3`–`ROI_90_mm3`, in numerical ROI order. `FileName`, `Original Name`, and labels are excluded.
3. NC=0 and AD=1. Fit `StandardScaler` only on training data, including independently within each CV fold.
4. Test labels are used for final evaluation of saved predictions; they do not participate in scaling, fitting, feature selection, or parameter selection.
5. No TIV normalization is applied; the SVM applies per-ROI standardization. All 10 test subjects are retained, including Data_44 with its documented BET limitations.

## Outputs

The `FileName` / `Prediction` columns of `results/test_predictions.csv` form the report prediction table. `test_evaluation.csv` compares predictions with supplied labels; `TrueLabel` is not a prediction. `AD_decision_score` is a signed SVM decision score, not a probability.

`training_record.json` records versions, CV scores, input SHA-256 hashes, label encoding, and scaler parameters. `svm_model.joblib` stores the model and feature order; load it with the same dependency versions. These results do not establish optimal settings or performance on other datasets.

Related pages: [English home](README.md), [English run results](RUN_RESULTS.md), [English report evidence](report_evidence/README.md).

References: [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html), [data leakage and Pipeline](https://scikit-learn.org/stable/common_pitfalls.html), [cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html).
