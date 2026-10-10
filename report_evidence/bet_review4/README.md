# Focused review: Data_33, Data_35, Data_36, and Data_44

[English](README.md) · [中文版](README_zh-CN.md)

The four `before_after.png` figures compare outputs before and after review. The `dense36` figures for 33/35/36 show sampled slices of the adopted candidates; `Data_44_retained_dense27.png` shows the retained output.

| Subject | Final BET options |
| --- | --- |
| Data_33 | `-f 0.55 -g -0.15 -c 116 158 82` |
| Data_35 | `-f 0.65 -g -0.075 -c 120 156 82` |
| Data_36 | `-f 0.45 -g 0 -c 92 175 82` |
| Data_44 | `-f 0.2 -g 0 -c 104 166 82` |

`review_decisions.json` records comparisons, quality notes, and selection reasons; `deployment.json` records the three updates and one retained subject. [selected_parameters_and_review.csv](selected_parameters_and_review.csv) provides the English review table. Review considered image boundaries and coverage, without disease labels or classification scores.

These are the adopted settings, not proof of mathematical optimality. Data_44's boundary issues remain in downstream processing and report notes. The earlier failed review and recommendation for correction are historical records; the agreed final workflow retained the existing result.
