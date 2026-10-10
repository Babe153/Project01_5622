# VM preprocessing: scripts and actual 3D outputs

[English](README.md) · [中文版](README_zh-CN.md)

Preprocessing for all 50 subjects, all 4500 ROI volumes, and SVM classification are complete. This directory stores the final outputs downloaded from the VM. `output_manifest.json` records each file's size and SHA-256; all 698 files were verified against the VM.

## Layout

- `scripts/`: five Bash files and final `bet_parameters.csv`. TODOs in the four main scripts are complete; `CreateSeedMask` preserves the instructor's original content.
- `Output/train/`: final outputs for Data_00–Data_39.
- `Output/test/`: final outputs for Data_40–Data_49.
- [Report evidence](../report_evidence/README.md): BET, tissue-segmentation and registration figures, plus logs.

## Run preprocessing

Place the six files from `scripts/` in the Linux project root, alongside `Data/train`, `Data/test`, and `Packages`. `Packages` requires `MNI152_T1_1mm_brain.nii.gz` and `aal.nii.gz`. Obtain original MRIs, templates, course documents, and software from the original course materials.

```bash
cd /home/elec5622/Project01
BET_DRY_RUN=1 bash SkullStripping
bash SkullStripping
bash TissueSegmentation
bash Registration
bash Measurement
```

`Measurement` calls `CreateSeedMask` automatically. Default software paths are `/home/elec5622/fsl` and `/home/elec5622/niftyreg/niftyreg_install`. Override `FSLDIR`, `NIFTYREG_INSTALL`, or `PROJECT_ROOT` for another installation or project directory.

These commands reprocess the inputs. The supplied final outputs are already complete and can be inspected directly. Run the local SVM from the repository root.

## Output files

| Example filename | Meaning |
| --- | --- |
| `Data_00_brain.nii.gz` | BET-extracted brain intensity image |
| `Data_00_brain_mask.nii.gz` | Binary BET brain mask |
| `Data_00_csf_mask.nii.gz` | Binary FAST CSF mask |
| `Data_00_greymatter_mask.nii.gz` | Binary FAST GM mask used for volume measurement |
| `Data_00_whitematter_mask.nii.gz` | Binary FAST WM mask |
| `Data_00_brain_greymatter.nii.gz` | Brain intensity image multiplied by the GM mask |
| `Data_00_brain_seg.nii.gz` | FAST discrete tissue classification |
| `Data_00_brain_mixeltype.nii.gz` | FAST mixed-tissue auxiliary classification |
| `Data_00_MNI_to_native_affine.txt` | Affine transformation from MNI template to native space |
| `Data_00_MNI_to_native_cpp.nii.gz` | Nonlinear control-point transformation; not an anatomical image |
| `Data_00_MNI_affine.nii.gz` | Affine-registered MNI template |
| `Data_00_MNI_warped.nii.gz` | Nonlinearly registered MNI template |
| `AAL_to_Data_00.nii.gz` | Native-space AAL atlas, resampled with nearest-neighbour interpolation |
| `AAL_statistics_volumn_train.csv` | Complete 40-subject, 90-feature training table; test has its corresponding table |
| `AAL_statistics_volumn_train_Data_XX.csv` | Single-subject intermediate CSV from parallel measurement; the final CSV is the merged table |

See the manifest for the actual file set. Individual ROI masks are generated temporarily and cleaned up during measurement. The retained native-space AAL image defines all regions and allows these masks to be recreated.

## View the outputs

GitHub previews PNGs. Download 3D `.nii.gz` files and open them in FSLeyes, for example from the preprocessing directory:

```bash
fsleyes Output/train/Data_00_brain.nii.gz Output/train/AAL_to_Data_00.nii.gz
```

Set a discrete label colour map and transparency for the AAL overlay, and inspect multiple directions. Add the GM mask to inspect tissue boundaries. Registration and measurement are in each subject's native space: the template and atlas are transformed to the subject, rather than all subject MRIs being transformed to MNI for measurement.

## Limitations

Data_44 retains the agreed output, including suspected frontal boundary omission and residual non-brain tissue. Passing numerical checks does not establish anatomically perfect segmentation. BET settings were not adjusted using test labels or SVM performance.
