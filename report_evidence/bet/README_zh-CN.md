[中文](README_zh-CN.md) · [English](README.md)

# 50 人最终 BET 效果

`images/` 中每人两张 PNG：`comparison` 展示原图边界、默认 BET 和最终 BET；`dense` 展示三个方向共 27 个位置的掩膜边界。每人的 JSON 和 `qc_manifest.json` 保存最终参数、切片位置和 NIfTI 校验值。全部 100 张图对应当前选定的 50 人 BET 结果。

下载整个仓库后可打开 [index.html](index.html) 逐人浏览。GitHub 页面直接点击 [images/](images/) 预览图片。

33、35、36 已在四人专项复核后更新正式结果；44 保留原结果，已知额部边界及非脑组织残留限制仍存在。最终执行参数以 [preprocessing/scripts/bet_parameters.csv](../../preprocessing/scripts/bet_parameters.csv) 为准。专项新旧对照图在 [bet_review4/](../bet_review4/)。

这是抽样切片视觉检查，没有人工标准掩膜，也没有逐层检查每个三维体素；不能据此称参数全局最优或分割完全准确。完整预处理与 SVM 已随后完成，当前整体状态见 [报告素材索引](../README_zh-CN.md)。
