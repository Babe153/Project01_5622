# Final report revision

The final academic report has 18 pages, 12 figures, three tables with three-line rules, and 10 references. The revision expands the rationale, methods and interpretation using existing experiment records. It does not change the preprocessing outputs, volume tables, model settings or predictions.

| Section | Revision |
| --- | --- |
| 1.1–1.2 | Explain the regional-feature representation, its tradeoffs, and how image processing and classification learning contribute to the project. |
| 3.1 | State NC/AD class counts, the fixed data split and recorded software environment. |
| 3.3 | Describe the actual visual criteria used for adopting BET parameters. |
| 3.7 | Add maximum-margin, soft-margin and support-vector concepts, with a distinction between the original method and software documentation. |
| 4.4 | Report checks of all 4500 volumes, numerical precision differences, nonzero ROI volumes and the scope of sampled manual review. |
| 5.1 | Interpret 39/40 out-of-fold and 9/10 test predictions, compare regional and voxel representations, and distinguish feature scaling from head-size adjustment. |
| 5.2–5.3 | Explain plausible preprocessing effects on features, the limits of small class counts and the scope of the conclusions. |
| Appendix A.5 | Identify the verification files and sampled FAST/registration subjects. |

The black-and-white workflow remains Figure 1 on page 3. The volume-extraction example remains Figure 2 on page 5. Table 3 on page 11 contains all ten test predictions. All ten references appear on page 14.

The additional references were verified against their publication records:

- [Cortes and Vapnik, Support-vector networks (1995)](https://link.springer.com/article/10.1007/BF00994018).
- [Barnes et al., Head size, age and gender adjustment in MRI studies (2010)](https://pubmed.ncbi.nlm.nih.gov/20600995/).

Numerical agreement does not establish anatomical ground truth. Sampled image review is not a review of every slice. No additional tuning, covariate adjustment or external validation is claimed.
