# 写报告的素材与证据索引

本索引对应已经实际运行的预处理和固定参数 SVM。它是写作材料说明，完整报告及真实成员贡献仍需另行整理。

## 建议使用的图片

| 报告位置 | 素材 | 能说明什么 |
| --- | --- | --- |
| 方法：总体流程 | [pipeline_overview.png](figures/pipeline_overview.png) | MRI→BET→FAST→配准/AAL→90 维体积→标准化/SVM |
| 方法/结果：BET | [Data_00_comparison.png](bet/images/Data_00_comparison.png) | 原图边界、默认提取和采用参数后的结果 |
| 方法：组织分割 | [Data_00_tissue.png](tissue_registration/Data_00_tissue.png) | GM、WM、CSF 的二值掩膜边界 |
| 方法：图谱配准 | [Data_00_registration.png](tissue_registration/Data_00_registration.png) | 仿射、非线性模板及 AAL 图谱与个人脑图的对应 |
| 结果：训练内验证 | [training_cv_accuracy.png](figures/training_cv_accuracy.png) | 五折准确率分别 100%、100%、100%、87.5%、100% |
| 结果：测试集 | [test_confusion_matrix.png](../results/test_confusion_matrix.png) | 真值按行、预测按列；顺序 NC、AD，矩阵 [[4,0],[1,5]] |
| 讨论：预处理局限 | [Data_44_dense.png](bet/images/Data_44_dense.png) 和 [Data_44_registration.png](tissue_registration/Data_44_registration.png) | 保留的 BET 边界问题和局部配准差异 |
| 讨论：参数复核 | [四人复核材料](bet_review4/) | 33、35、36 更新、44 保留的过程依据 |

代表图只用于展示流程；50 人的全部 BET 图在 `bet/images/`，全部组织分割和配准图在 `tissue_registration/`。下载后可打开两处 `index.html` 切换受试者。HTML 是本地浏览器，不会在 GitHub 文件页直接执行。

## 可直接核实的数据与证据

- [每人 90 个体积的提交表](../submission/Project01_90脑区灰质体积.xlsx)：Train 40 人、Test 10 人，共 4500 个灰质体积值，单位 mm³。
- [测试预测与真值对照](../results/test_evaluation.csv)：10 人预测及是否正确，Data_49 是唯一错分者（标签 AD，预测 NC）。
- [测试指标](../results/test_metrics.json)：90% 准确率，AD 敏感度 83.3%，NC 特异度 100%。
- [训练记录](../results/training_record.json)：固定 SVM 参数、五折分数、标准化统计量、训练样本和依赖版本。
- [代码验证](../results/code_verification.json)：Notebook/CLI 一致、模型重载一致、标签/特征按 ID 对齐以及测试标签不参与拟合的验证。
- [流水线状态](validation/status.json) 和 [执行日志](validation/pipeline_execution.log)：正式任务完成记录；`validation/logs/` 包含逐人的 FAST、配准和测量日志。
- [体积独立核对](validation/volume_verification.json)：从二值掩膜独立数体素并乘体素体积，与 FSL 的 4500 个结果逐一比较；最大绝对差约 0.000906 mm³，为输出舍入差异。
- [BET 正式结果核对](bet/validation/formal_verification.json)：参数表、二值掩膜、原图乘掩膜及所选结果的一致性。
- [实际三维输出及 SHA-256](../preprocessing/output_manifest.json)：全部 698 个文件均与虚拟机最终 Output 核对。
- [实际脚本](../preprocessing/scripts/)：五个 Bash 文件和逐人 BET 参数。`CreateSeedMask` 保持老师原始版本。
- [处理质量备注](../submission/处理与检查记录.csv) 和 [人工抽样复核记录](validation/visual_review.json)：区分数值检查与人工图像检查。

## 方法部分应准确描述的设置

1. 固定划分：Data_00～39 训练（40 人，NC 21 / AD 19），Data_40～49 测试（10 人，NC 4 / AD 6）。
2. BET 读取逐人的 `f`、`g` 和可选 `c`。中心是原始图像体素坐标，不是 mm，也不等于 RAS 展示切片编号。
3. FAST 使用老师示例 `-S 1 -n 3 -t 1 -g -v`。灰质、白质、脑脊液使用二值掩膜，灰质强度图由脑图乘 GM 掩膜生成。
4. `reg_aladin` 做模板到个人脑图的仿射配准；`reg_f3d` 从仿射初始化做非线性配准；`reg_resample -inter 0` 把 AAL 标签传播到个人空间。
5. AAL 编号 1～90 的区域与 GM 二值掩膜相交，`fslstats -V` 输出非零体素物理体积。不是概率加权灰质体积；未做颅内容积归一化。
6. 模型是 `Pipeline(StandardScaler(), SVC(kernel='rbf', C=1, gamma='scale'))`，90 个体积特征，NC=0、AD=1。ID 和标签不进入特征矩阵。
7. 训练内 `StratifiedKFold(n_splits=5, shuffle=True, random_state=73)`；每折 scaler 只用该折训练数据拟合，再在全部 40 人上训练最终模型。没有网格搜索或测试集调参。
8. 先对 10 人保存预测，再用提供的测试标签评估。五折平均准确率 97.5%，各折标准差 5 个百分点；训练拟合准确率 100% 不等于泛化表现。

## 检查能支持到什么程度

50 人均完成文件、几何、数值和体积算术检查。BET 看过每人的抽样多方向图片；FAST/配准的人工抽样复核为 00、01、15、18、33、35、36、40、44、49 共 10 人。不要把它写成“50 人所有切片人工检查通过”或“50 人解剖分割完全准确”。

Data_44 有额部边界疑似遗漏及非脑组织残留，保留结果继续测量；图像质量与局部配准差异可能影响体积。Data_49 的错分原因尚未证实，不应直接归因于某个脑区或预处理步骤。测试仅 10 人，每错一人准确率变化 10 个百分点；目前没有独立外部测试集。决策分数不是疾病概率。

## 软件与参考资料

实际环境为 FSL 6.0.7.1、NiftyReg 1.5.58、Python 3.12；Python 固定版本见根目录 `requirements.txt`，运行记录见 `training_record.json`。写正式报告时需按课程格式引用算法原始论文或官方资料；以下是查参数与工具行为的入口：

- [FSL BET 官方文档](https://fsl.fmrib.ox.ac.uk/fsl/docs/structural/bet.html)
- [FSL FAST 官方文档](https://fsl.fmrib.ox.ac.uk/fsl/docs/structural/fast.html)
- [scikit-learn SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
- [scikit-learn 数据泄漏说明](https://scikit-learn.org/stable/common_pitfalls.html)

报告还需要真实组员姓名、学号和各自贡献，以及正文、图题和参考文献。目前仓库中的图、日志和指标已经足以支持本次实际方法与结果的写作。
