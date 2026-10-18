# Final report revision

The report title is **Classifying AD Patients and Normal Controls from Brain Images**, aligned with the assignment name. The title and abstract occupy page 1, followed by a linked two-level **Contents** page on page 2. All 35 entries were checked against Word pagination. The main text begins on page 3; subsequent body pages retain the reviewed layout with updated page numbers.

Page 1 uses a restrained academic layout with a course label, balanced title lines, an italic methods subtitle, separate author lines, an independent Abstract heading and keywords. The abstract prose is preserved. Pages 2–22 are identical in both text and rendered appearance to the reviewed contents edition, and all directory page references remain correct.

The front page also includes a clickable **Code and data availability** link to [Babe153/Project01_5622](https://github.com/Babe153/Project01_5622), identifying the preprocessing scripts, SVM notebook, ROI volume tables and verification records. The link target was verified in the Word file and its rendered PDF. This addition retains all 22 pages and the directory page numbers.

The enhanced academic report has **22 pages, 13 figures, four native Word tables with three-line rules, and 12 references**. The original 12 figures, three tables, academic styles and page settings are retained. This revision adds a training-only descriptive analysis and strengthens the connection between experimental evidence and literature. Preprocessing outputs, the submitted volume workbook, SVM settings and predictions remain unchanged.

| Section | Main enhancement |
| --- | --- |
| Abstract and 1.1–1.2 | State the purpose, representation tradeoff, course learning contributions and scope of the findings. |
| 3.4 | Explain spatial tissue-label dependence and estimation in FAST; distinguish binary GM volume from intensity or probability sums. |
| 3.5–3.6 | Explain affine/nonlinear roles, label interpolation and native-space physical volume without normalized-GM Jacobian modulation. Retain the real extraction example. |
| 3.7 | Explain RBF similarity, scaling, C, gamma, soft margins and support vectors; distinguish original SVM theory from implementation documentation. |
| 3.8 | Define the post hoc training-only GM-scale, regional-fraction, pooled-SD effect and native-header analyses. |
| 4.4 | Retain verification of all 4500 volumes and distinguish numerical checks from sampled anatomical review. |
| 4.7 | Add Table 4 and Figure 8: training volume summaries, all 90 regional contrasts and the class-associated geometry finding. |
| 5.1 | Synthesize findings with regional atrophy, voxel-SVM, review and ICV-adjustment sources. Explain shared-denominator effects and why stratified folds do not resolve geometry-associated differences. |
| 5.2–5.3 | Distinguish reproducible arithmetic, anatomical plausibility and predictive correctness; prioritize acquisition/covariate assessment and new independent evaluation. Distinguish classification from probability calibration and clinical utility. |
| Appendix A | Retain processing/classification commands, verification records and the new analysis command. |

## Reading map

- Contents, page 2: 35 linked entries with right-aligned page numbers and dot leaders.
- Figure 1, page 5: black-and-white overall workflow.
- Figure 2, page 7: actual Data_00 regional GM volume extraction.
- Table 3 and Figure 7, page 13: all ten predictions and the confusion matrix.
- Table 4 and Figure 8, page 14: training-only descriptive supplement.
- Sections 5.1–5.3, pages 15–17: interpretation, limitations and conclusion.
- References, page 18: all 12 entries.
- Appendix A, pages 19–20; Appendix B, pages 21–22.

The former Data_44 Figure 8 is now Figure 9, on page 16. Its original image is retained. Figure B4 provides the enlarged view on page 22.

## Added evidence

See [training analysis](../report_evidence/training_analysis/README.md) for source code, subject summaries, all 90 effects, native-mask header audit, input hashes and PNG/SVG figure. This supplement is explicitly post hoc and does not select inputs or change the classifier.

The added sources were checked against their original publication records:

- [Voevodskaya et al., volume adjustment experiments (2014)](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2014.00264/full).
- [Collins et al., TRIPOD+AI reporting guidance (2024)](https://www.bmj.com/content/385/bmj-2023-078378).

Numerical agreement does not establish anatomical ground truth. Regional GM-sum fractions are not ICV adjustment. Class-associated geometry does not establish scanner identity or explain predictions causally. No new model-comparison, calibrated-probability or external-validation claim is made.

The Contents page is a native Word TOC field with heading links and page-reference fields. After later edits, right-click the directory and choose **Update Field → Update entire table**. Its Times New Roman font, black text, two levels, dot leaders and right-aligned page numbers match the academic report layout.
