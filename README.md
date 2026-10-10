# Repo for 2026S2 Project01_elec5622

## Project01：90 个 AAL 脑区灰质体积的 SVM 分类

预处理脚本与全部三维输出、报告素材、Notebook、命令行脚本、配套数据和一次实际运行结果已整理在此仓库。模型使用 `StandardScaler + SVC(kernel="rbf", C=1, gamma="scale")`，参数固定，没有按测试标签调参。

### 文件入口

| 文件 | 用途 |
| --- | --- |
| [Project01_SVM.ipynb](Project01_SVM.ipynb) | 按 Lab 2 步骤组织的 Notebook，含中文解释和已执行输出 |
| [project01_svm.py](project01_svm.py) | 命令行训练、预测及可选评估；Notebook 共用的数据读取函数 |
| [README_运行说明.md](README_运行说明.md) | VSCode 环境、运行步骤和与 Lab 2 的对应关系 |
| [data/](data/) | 训练/测试体积 CSV 和 `data_labels.csv` |
| [submission/Project01_90脑区灰质体积.xlsx](submission/Project01_90脑区灰质体积.xlsx) | 作业提交用的体积表，Train/Test 两张工作表覆盖全部 50 人 |
| [results/test_predictions.csv](results/test_predictions.csv) | Data_40.nii～Data_49.nii 的 AD/NC 预测表 |
| [运行结果说明.md](运行结果说明.md) | 实际运行指标与逐人预测对照 |

### 数据划分和表格含义

- 训练集：Data_00～Data_39，共 40 人；测试集：Data_40～Data_49，共 10 人。
- 每人 90 个特征，为 AAL 编号 1～90 的灰质二值掩膜体积，单位 mm³。
- 训练/测试 CSV 和提交用 Excel 均为 91 列：`FileName` + `ROI_1_mm3`～`ROI_90_mm3`。FileName 仅用于对齐，不进入特征矩阵。
- 标签通过 `data_labels.csv` 的 `New Name` 对齐，去掉空格和 .nii 后缀；NC=0，AD=1。
- 标准化只使用训练数据；训练内五折交叉验证也在每折内独立拟合 scaler。测试标签仅用于最后评估。
- 50×90 个体积值已经独立核对。`submission/` 中同时保存数值检查、Excel 检查和预处理质量备注。

### 本地运行

已在 Python 3.12 验证。先克隆仓库并进入目录，再创建环境、安装依赖：

```powershell
git clone https://github.com/Babe153/Project01_5622.git
cd Project01_5622
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe project01_svm.py --evaluate
```

如果使用其它受支持的 Python，可把创建环境的命令换成 `python -m venv .venv`。也可以在 VSCode 打开仓库文件夹，选择该环境作为 Notebook 内核，从上到下运行 `Project01_SVM.ipynb`。不需要在本地安装 FSL。

不对照测试标签时，去掉 `--evaluate`；脚本仍然训练模型并保存预测。再次运行会更新 `results/`。

### 已验证结果

- 训练集准确率：100%（训练拟合情况）。
- 训练集内五折 CV 平均准确率：97.5%；各折准确率标准差 5 个百分点。
- 最后测试准确率：90%，正确 9/10 人。Data_49 被预测为 NC，提供的标签为 AD。
- AD sensitivity：83.3%；NC specificity：100%。
- Notebook 和脚本的预测、CV 分数一致；模型重载后预测一致。

这些是固定基线在本作业数据上的结果。Data_44 沿用已确认的 BET 结果，其已知预处理边界限制记录在 `submission/处理与检查记录.csv`。测试集仅 10 人，不据此宣称参数最优或其它人群上的性能。

API 参考：[SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)、[Pipeline 与数据泄漏](https://scikit-learn.org/stable/common_pitfalls.html)。

### 新增：虚拟机预处理与报告素材

- [preprocessing/](preprocessing/README.md)：五个 Bash 脚本、最终 BET 参数、全部 50 人三维处理输出（约 623 MiB），以及逐文件 SHA-256。
- [report_evidence/](report_evidence/README.md)：100 张 BET 图、100 张 FAST/配准图、8 张专项复核图、流程图、CV 图和实际运行日志；索引说明报告引用位置与质量限制。
- `.nii.gz` 需下载后用 FSLeyes 查看；PNG 可直接在 GitHub 预览。下载整个仓库后可打开 HTML 逐人浏览。
- 原始 MRI、课程 PDF 和模板安装包仍使用老师提供的原始材料。
