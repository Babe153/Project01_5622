# Report figures and supporting evidence

[English](README.md) · [中文版](README_zh-CN.md)

This index describes the completed preprocessing and fixed-baseline SVM. It supplies writing materials; the full report and actual team contributions still need to be prepared.

For per-subject preprocessing pictures, open the [50-subject image gallery](../preprocessing/figures/README.md).

The [detailed project workflow](figures/project_workflow_en.png) explains every step, script, input, and output. It is also embedded near the top of the home README.

## Suggested figures

| Report section | Figure | What it demonstrates |
| --- | --- | --- |
| Methods: workflow | [pipeline_overview.png](figures/pipeline_overview.png) | MRI → BET → FAST → registration/AAL → 90 volumes → scaling/SVM |
| Methods/Results: BET | [Data_00_comparison.png](bet/images/Data_00_comparison.png) | Original-image boundary, default extraction, and selected-parameter extraction |
| Methods: tissue segmentation | [Data_00_tissue.png](tissue_registration/Data_00_tissue.png) | Binary GM, WM, and CSF mask boundaries |
| Methods: atlas registration | [Data_00_registration.png](tissue_registration/Data_00_registration.png) | Affine/nonlinear template and AAL alignment with the native brain |
| Results: training validation | [training_cv_accuracy.png](figures/training_cv_accuracy.png) | Five fold accuracies: 100%, 100%, 100%, 87.5%, 100% |
| Results: test performance | [test_confusion_matrix.png](../results/test_confusion_matrix.png) | True classes as rows, predictions as columns; NC/AD order; [[4,0],[1,5]] |
| Discussion: preprocessing limitations | [Data_44_dense.png](bet/images/Data_44_dense.png) and [Data_44_registration.png](tissue_registration/Data_44_registration.png) | Retained BET boundary issues and local registration differences |
| Discussion: parameter review | [Four-subject review](bet_review4/) | Evidence for updating 33/35/36 and retaining 44 |

Representative figures illustrate the workflow. All 50 subjects' BET figures are in `bet/images/`; all tissue/registration figures are in `tissue_registration/`. After downloading the repository, open either `index.html` to switch subjects. GitHub's file view does not execute these HTML browsers.

## Data and verification records

- [Submission volume workbook](../submission/Project01_90_ROI_GM_volumes.xlsx): Train 40 / Test 10, 4500 GM volumes in mm³.
- [Test predictions and labels](../results/test_evaluation.csv): all 10 predictions and correctness; Data_49 is the sole error (AD label, NC prediction).
- [Test metrics](../results/test_metrics.json): 90% accuracy, 83.3% AD sensitivity, and 100% NC specificity.
- [Training record](../results/training_record.json): fixed parameters, CV scores, scaler statistics, training subjects, and dependency versions.
- [Code verification](../results/code_verification.json): notebook/CLI agreement, model reload agreement, ID-based alignment, and independence from test labels.
- [Pipeline status](validation/status.json) and [execution log](validation/pipeline_execution.log): completed execution; `validation/logs/` contains subject-level FAST, registration, and measurement logs.
- [Independent volume verification](validation/volume_verification.json): independently counted mask voxels multiplied by voxel volume, checked against all 4500 FSL outputs. Maximum absolute difference is approximately 0.000906 mm³, attributable to output rounding.
- [Formal BET verification](bet/validation/formal_verification.json): agreement of parameters, binary masks, raw image × mask, and selected outputs.
- [3D output manifest](../preprocessing/output_manifest.json): all 698 files verified against the final VM Output directory.
- [Actual scripts](../preprocessing/scripts/): five Bash files and per-subject BET settings; `CreateSeedMask` is the instructor's unchanged original.
- [Processing QC notes](../submission/processing_qc_records.csv) and [manual sampled review](validation/visual_review.json): distinguish numerical checks from manual image inspection.

## Settings to describe accurately

1. Fixed split: Data_00–39 train (40; NC 21 / AD 19), Data_40–49 test (10; NC 4 / AD 6).
2. BET reads per-subject `f`, `g`, and optional `c`. The centre uses original-image voxel coordinates, not mm or RAS display slice indices.
3. FAST uses the instructor's example options `-S 1 -n 3 -t 1 -g -v`. GM, WM, and CSF masks are binary; the GM intensity image is brain × GM mask.
4. `reg_aladin` maps the template to the subject with affine registration; `reg_f3d` performs nonlinear refinement initialized by that affine; `reg_resample -inter 0` propagates AAL labels into native space.
5. AAL labels 1–90 intersect the binary GM mask. `fslstats -V` provides nonzero-voxel physical volumes. These are not probability-weighted volumes; no intracranial-volume normalization is applied.
6. `Pipeline(StandardScaler(), SVC(kernel='rbf', C=1, gamma='scale'))`, 90 volume features, NC=0 / AD=1. IDs and labels are excluded from the features.
7. Training-only `StratifiedKFold(n_splits=5, shuffle=True, random_state=73)` fits the scaler within each training fold; the final pipeline is fitted on all 40. No grid search or test-set tuning is performed.
8. Predictions are saved before evaluating supplied test labels. CV mean accuracy is 97.5%, fold standard deviation is 5 percentage points; 100% training fit accuracy is not a generalization estimate.

## Scope of quality checks

All 50 subjects passed file, geometry, numerical, and volume-arithmetic checks. Sampled multidirectional BET figures were reviewed for each subject. Manual sampled FAST/registration review covered 10 subjects: 00, 01, 15, 18, 33, 35, 36, 40, 44, and 49. This does not amount to manually checking every slice of all 50 subjects or proving anatomical perfection.

Data_44 retains suspected frontal omission and non-brain remnants; image quality and local registration differences may affect volumes. The cause of the Data_49 classification error has not been established and should not be attributed to a particular ROI or preprocessing stage without evidence. The test set contains only 10 subjects; one error changes accuracy by 10 percentage points. There is no independent external test set. Decision scores are not disease probabilities.

Historical BET review notes record the earlier recommendation to correct Data_44. The agreed workflow subsequently retained that result and completed measurement; the limitation remains documented.

## Software and references

Actual environments: FSL 6.0.7.1, NiftyReg 1.5.58, and Python 3.12. Pinned Python versions are in root `requirements.txt`; actual run versions are in `results/training_record.json`. Cite original algorithm papers or official resources in the course's required style. Parameter/documentation entry points:

- [FSL BET](https://fsl.fmrib.ox.ac.uk/fsl/docs/structural/bet.html)
- [FSL FAST](https://fsl.fmrib.ox.ac.uk/fsl/docs/structural/fast.html)
- [scikit-learn SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
- [scikit-learn data leakage guidance](https://scikit-learn.org/stable/common_pitfalls.html)

The report still needs actual member names, student IDs, contributions, text, figure captions, and references. The supplied figures, logs, and metrics support the implemented methods and results.
