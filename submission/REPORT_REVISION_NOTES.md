# Final report revision

The enhanced academic report has **20 pages, 13 figures, four native Word tables with three-line rules, and 12 references**. The original 12 figures, three tables, academic styles and page settings are retained. This revision adds a training-only descriptive analysis and strengthens the connection between experimental evidence and literature. Preprocessing outputs, the submitted volume workbook, SVM settings and predictions remain unchanged.

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

- Figure 1, page 3: black-and-white overall workflow.
- Figure 2, page 5: actual Data_00 regional GM volume extraction.
- Table 3 and Figure 7, page 11: all ten predictions and the confusion matrix.
- Table 4 and Figure 8, page 12: training-only descriptive supplement.
- Sections 5.1–5.3, pages 13–15: interpretation, limitations and conclusion.
- References, page 16: all 12 entries.
- Appendix A, pages 17–18; Appendix B, pages 19–20.

The former Data_44 Figure 8 is now Figure 9, on page 14. Its original image is retained. Figure B4 provides the enlarged view on page 20.

## Added evidence

See [training analysis](../report_evidence/training_analysis/README.md) for source code, subject summaries, all 90 effects, native-mask header audit, input hashes and PNG/SVG figure. This supplement is explicitly post hoc and does not select inputs or change the classifier.

The added sources were checked against their original publication records:

- [Voevodskaya et al., volume adjustment experiments (2014)](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2014.00264/full).
- [Collins et al., TRIPOD+AI reporting guidance (2024)](https://www.bmj.com/content/385/bmj-2023-078378).

Numerical agreement does not establish anatomical ground truth. Regional GM-sum fractions are not ICV adjustment. Class-associated geometry does not establish scanner identity or explain predictions causally. No new model-comparison, calibrated-probability or external-validation claim is made.
