# Final BET results for 50 subjects

[English](README.md) · [中文版](README_zh-CN.md)

`images/` contains two PNGs per subject: `comparison` shows original-image boundaries, default BET, and final BET; `dense` shows mask boundaries at 27 positions across three directions. Per-subject JSON files and `qc_manifest.json` record final parameters, slice locations, and NIfTI checksums. All 100 figures correspond to the current selected BET outputs.

After downloading the repository, open [index.html](index.html) to browse subjects. On GitHub, open [images/](images/) to preview figures.

Data_33, Data_35, and Data_36 were updated after the four-subject review. Data_44 retains the previous output and its known frontal-boundary/non-brain-remnant limitations. Final execution settings are in [bet_parameters.csv](../../preprocessing/scripts/bet_parameters.csv); before/after figures are in [bet_review4/](../bet_review4/).

This is visual inspection of sampled slices, without manual ground-truth masks or review of every 3D voxel. It does not establish globally optimal parameters or perfect segmentation. The complete preprocessing and SVM were subsequently completed; see the [report evidence index](../README.md).

The review notes include historical recommendations made before the agreed decision to retain Data_44 for the completed pipeline. English QC notes are in [parameters_and_qc_records.csv](parameters_and_qc_records.csv).
