# Report structure and verification

The report, **Classifying AD Patients and Normal Controls from Brain Images**, describes the ELEC5622 Project 1 experiment. [Read the PDF report](ELEC5622_Project01_Academic_Report_BW.pdf) or [download the Word report](ELEC5622_Project01_Academic_Report_BW.docx).

The report has 22 pages, 13 figures, four three-line tables and 12 references. A linked contents page follows the title and abstract. The front page links to the repository for code, volume tables and verification records.

## Section map

| Section | Contents and experimental stage |
| --- | --- |
| 1 Aims and Background | AD-related structural changes, MRI classification, regional features and the project aims. |
| 2 Contributions | Team members and their reported responsibilities. |
| 3 Methodology | BET brain extraction, FAST tissue segmentation, affine/nonlinear atlas registration, native-space GM volumes and the fixed SVM pipeline. Section 3.8 defines the post hoc training-only supplement. |
| 4 Results | Image examples, volume checks, cross-validation, all ten test predictions and the training-only volume/geometry findings. |
| 5 Discussion and Conclusion | Interpretation alongside prior research, preprocessing limitations, small-sample uncertainty and class-associated image geometry. |
| References | Twelve publications and implementation resources cited in the report. |
| Appendix A | Processing, classification and verification commands and records. |
| Appendix B | Enlarged preprocessing figures. |

## Key figures and tables

- Figure 1, page 5: black-and-white overall workflow.
- Figure 2, page 7: Data_00 ROI volume extraction from actual masks.
- Table 3 and Figure 7, page 13: ten predictions and the confusion matrix.
- Table 4 and Figure 8, page 14: post hoc training-only volume and geometry analysis.
- Figure 9, page 16: the retained Data_44 BET boundary limitation.
- References, page 18; Appendix A, pages 19–20; Appendix B, pages 21–22.

## Reproducibility and scope

The [evidence index](../report_evidence/README.md) links the figures, execution logs and numerical checks. The [training analysis](../report_evidence/training_analysis/README.md) includes code, subject summaries, all 90 regional effects, image-header checks and input hashes. This descriptive supplement does not select inputs or change the classifier.

All 4500 exported volumes were checked independently against the masks. Sampled BET figures were reviewed for all 50 subjects; sampled FAST/registration review covered ten subjects. Numerical agreement does not establish anatomical ground truth. Data_44 retains its documented boundary limitation. Regional GM-sum fractions are not ICV adjustment, and class-associated geometry does not establish scanner identity or causation. The fixed baseline's test accuracy is 9/10; there is no independent external validation.

The Word contents page uses native TOC and page-reference fields. After later edits, right-click the contents and choose **Update Field → Update entire table**, then check pagination.

The PDF was exported directly from the final Word document. All 22 rendered pages match the verified Word layout; all 35 contents links and page numbers were checked. The accompanying workbook uses white backgrounds, black text, bold headers and three horizontal rules. Both sheets retain their native tables, filters, frozen header/ID panes and all 4500 measured values.
