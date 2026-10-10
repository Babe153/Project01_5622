# 预处理阶段图片索引

[中文](README_zh-CN.md) · [English](README.md)

全部 50 人的预处理 PNG 已上传：100 张 BET 图、100 张组织分割/配准图。本页逐人链接到所有图片；本文件夹也保存了代表图，可直接查看。全部逐人原尺寸图片位于 `report_evidence/`。

## 代表图

### Data_00：BET 脑部提取

三行依次为原图加采用掩膜的边界、默认 BET、采用参数后的 BET。

![Data_00 BET 比较图](Data_00_bet_comparison.png)

### Data_00：FAST 组织分割

三行分别为灰质 GM（红边）、白质 WM（青边）、脑脊液 CSF（黄边）的二值掩膜边界。

![Data_00 组织分割](Data_00_tissue.png)

### Data_00：配准及 AAL 标签

三行分别为仿射模板、非线性模板和个人空间中的 AAL 离散标签叠加。

![Data_00 配准及 AAL 叠加](Data_00_registration.png)

### Data_44：已记录的 BET 局限

保留结果仍有额部脑组织疑似遗漏及非脑组织残留，属于最终数据中已记录的质量限制。

![Data_44 保留的 BET 掩膜](Data_44_bet_dense.png)

## 全部受试者

点击 PNG 链接可在 GitHub 预览。下载仓库后，可打开 [BET 浏览器](../../report_evidence/bet/index.html) 和 [组织分割/配准浏览器](../../report_evidence/tissue_registration/index.html) 离线切换受试者；GitHub 的 HTML 文件页不会直接执行这些浏览器。

| 受试者 | 分组 | BET 比较图 | BET 27 切片掩膜 | FAST 组织掩膜 | 配准 / AAL |
| --- | --- | --- | --- | --- | --- |
| Data_00 | 训练 | [比较图](../../report_evidence/bet/images/Data_00_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_00_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_00_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_00_registration.png) |
| Data_01 | 训练 | [比较图](../../report_evidence/bet/images/Data_01_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_01_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_01_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_01_registration.png) |
| Data_02 | 训练 | [比较图](../../report_evidence/bet/images/Data_02_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_02_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_02_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_02_registration.png) |
| Data_03 | 训练 | [比较图](../../report_evidence/bet/images/Data_03_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_03_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_03_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_03_registration.png) |
| Data_04 | 训练 | [比较图](../../report_evidence/bet/images/Data_04_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_04_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_04_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_04_registration.png) |
| Data_05 | 训练 | [比较图](../../report_evidence/bet/images/Data_05_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_05_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_05_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_05_registration.png) |
| Data_06 | 训练 | [比较图](../../report_evidence/bet/images/Data_06_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_06_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_06_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_06_registration.png) |
| Data_07 | 训练 | [比较图](../../report_evidence/bet/images/Data_07_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_07_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_07_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_07_registration.png) |
| Data_08 | 训练 | [比较图](../../report_evidence/bet/images/Data_08_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_08_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_08_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_08_registration.png) |
| Data_09 | 训练 | [比较图](../../report_evidence/bet/images/Data_09_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_09_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_09_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_09_registration.png) |
| Data_10 | 训练 | [比较图](../../report_evidence/bet/images/Data_10_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_10_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_10_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_10_registration.png) |
| Data_11 | 训练 | [比较图](../../report_evidence/bet/images/Data_11_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_11_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_11_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_11_registration.png) |
| Data_12 | 训练 | [比较图](../../report_evidence/bet/images/Data_12_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_12_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_12_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_12_registration.png) |
| Data_13 | 训练 | [比较图](../../report_evidence/bet/images/Data_13_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_13_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_13_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_13_registration.png) |
| Data_14 | 训练 | [比较图](../../report_evidence/bet/images/Data_14_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_14_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_14_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_14_registration.png) |
| Data_15 | 训练 | [比较图](../../report_evidence/bet/images/Data_15_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_15_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_15_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_15_registration.png) |
| Data_16 | 训练 | [比较图](../../report_evidence/bet/images/Data_16_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_16_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_16_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_16_registration.png) |
| Data_17 | 训练 | [比较图](../../report_evidence/bet/images/Data_17_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_17_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_17_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_17_registration.png) |
| Data_18 | 训练 | [比较图](../../report_evidence/bet/images/Data_18_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_18_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_18_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_18_registration.png) |
| Data_19 | 训练 | [比较图](../../report_evidence/bet/images/Data_19_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_19_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_19_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_19_registration.png) |
| Data_20 | 训练 | [比较图](../../report_evidence/bet/images/Data_20_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_20_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_20_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_20_registration.png) |
| Data_21 | 训练 | [比较图](../../report_evidence/bet/images/Data_21_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_21_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_21_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_21_registration.png) |
| Data_22 | 训练 | [比较图](../../report_evidence/bet/images/Data_22_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_22_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_22_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_22_registration.png) |
| Data_23 | 训练 | [比较图](../../report_evidence/bet/images/Data_23_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_23_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_23_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_23_registration.png) |
| Data_24 | 训练 | [比较图](../../report_evidence/bet/images/Data_24_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_24_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_24_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_24_registration.png) |
| Data_25 | 训练 | [比较图](../../report_evidence/bet/images/Data_25_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_25_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_25_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_25_registration.png) |
| Data_26 | 训练 | [比较图](../../report_evidence/bet/images/Data_26_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_26_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_26_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_26_registration.png) |
| Data_27 | 训练 | [比较图](../../report_evidence/bet/images/Data_27_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_27_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_27_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_27_registration.png) |
| Data_28 | 训练 | [比较图](../../report_evidence/bet/images/Data_28_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_28_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_28_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_28_registration.png) |
| Data_29 | 训练 | [比较图](../../report_evidence/bet/images/Data_29_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_29_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_29_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_29_registration.png) |
| Data_30 | 训练 | [比较图](../../report_evidence/bet/images/Data_30_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_30_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_30_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_30_registration.png) |
| Data_31 | 训练 | [比较图](../../report_evidence/bet/images/Data_31_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_31_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_31_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_31_registration.png) |
| Data_32 | 训练 | [比较图](../../report_evidence/bet/images/Data_32_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_32_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_32_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_32_registration.png) |
| Data_33 | 训练 | [比较图](../../report_evidence/bet/images/Data_33_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_33_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_33_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_33_registration.png) |
| Data_34 | 训练 | [比较图](../../report_evidence/bet/images/Data_34_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_34_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_34_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_34_registration.png) |
| Data_35 | 训练 | [比较图](../../report_evidence/bet/images/Data_35_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_35_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_35_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_35_registration.png) |
| Data_36 | 训练 | [比较图](../../report_evidence/bet/images/Data_36_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_36_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_36_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_36_registration.png) |
| Data_37 | 训练 | [比较图](../../report_evidence/bet/images/Data_37_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_37_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_37_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_37_registration.png) |
| Data_38 | 训练 | [比较图](../../report_evidence/bet/images/Data_38_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_38_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_38_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_38_registration.png) |
| Data_39 | 训练 | [比较图](../../report_evidence/bet/images/Data_39_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_39_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_39_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_39_registration.png) |
| Data_40 | 测试 | [比较图](../../report_evidence/bet/images/Data_40_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_40_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_40_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_40_registration.png) |
| Data_41 | 测试 | [比较图](../../report_evidence/bet/images/Data_41_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_41_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_41_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_41_registration.png) |
| Data_42 | 测试 | [比较图](../../report_evidence/bet/images/Data_42_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_42_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_42_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_42_registration.png) |
| Data_43 | 测试 | [比较图](../../report_evidence/bet/images/Data_43_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_43_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_43_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_43_registration.png) |
| Data_44 | 测试 | [比较图](../../report_evidence/bet/images/Data_44_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_44_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_44_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_44_registration.png) |
| Data_45 | 测试 | [比较图](../../report_evidence/bet/images/Data_45_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_45_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_45_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_45_registration.png) |
| Data_46 | 测试 | [比较图](../../report_evidence/bet/images/Data_46_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_46_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_46_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_46_registration.png) |
| Data_47 | 测试 | [比较图](../../report_evidence/bet/images/Data_47_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_47_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_47_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_47_registration.png) |
| Data_48 | 测试 | [比较图](../../report_evidence/bet/images/Data_48_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_48_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_48_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_48_registration.png) |
| Data_49 | 测试 | [比较图](../../report_evidence/bet/images/Data_49_comparison.png) | [掩膜图](../../report_evidence/bet/images/Data_49_dense.png) | [组织分割](../../report_evidence/tissue_registration/Data_49_tissue.png) | [配准图](../../report_evidence/tissue_registration/Data_49_registration.png) |
