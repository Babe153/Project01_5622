# Project01 SVM

用 AAL 前 90 个脑区的灰质体积预测 AD/NC。此目录在本地 Windows / VSCode 上运行；不需要 FSL，也不需要连接虚拟机。

## 文件

- `Project01_SVM.ipynb`：按 Lab 2 的步骤逐段运行，附中文解释；正式训练、预测与最后评估的代码均已完成。
- `project01_svm.py`：相同模型的命令行版本，也提供 Notebook 共用的文件读取和结果保存函数。
- `data/`：训练集 40 人的体积、测试集 10 人的体积，以及原始标签表的副本。
- `requirements.txt`：Python 依赖。
- `results/`：一次实际运行的预测、指标、混淆矩阵和模型；再次运行会更新该目录。

## VSCode 运行

1. 在 VSCode 使用“打开文件夹”打开整个 SVM 目录。
2. 在该目录的终端创建并选择 Python 环境（推荐 Python 3.12）：

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

如果电脑只有其它受支持的 Python 版本，可以把第一行换成 `python -m venv .venv`。VSCode 的 Python/Jupyter 扩展需要已安装。Notebook 内核选择本目录 `.venv`；命令行直接调用它的 Python，无需执行激活脚本。

3. 打开 `Project01_SVM.ipynb`，从上到下运行。Notebook 的 `EVALUATE_TEST=True` 会在模型训练和预测保存之后，对照已提供的测试标签。

命令行只训练和导出预测：

```powershell
.\.venv\Scripts\python.exe project01_svm.py
```

训练、预测并最后评估：

```powershell
.\.venv\Scripts\python.exe project01_svm.py --evaluate
```

可用 `--train`、`--test`、`--labels` 和 `--output-dir` 指定其它路径；默认路径相对脚本所在目录，所以从其它工作目录运行脚本也能找到数据。

## 与 Lab 2 / Project01 的对应关系

| Lab 2 的步骤 | 本项目代码 |
| --- | --- |
| Import APIs and Load PIMA | 导入 `sklearn.svm`，读两份体积表，按 New Name 匹配 AD/NC 标签 |
| train_test_split | 使用 Project01 规定的 Data_00～39 / Data_40～49 划分 |
| SVM TODO | `svm.SVC(...).fit(...)`，通过 Pipeline 先做 StandardScaler |
| Output accuracy | 单独输出训练准确率、训练内五折 CV 准确率和最终测试准确率 |

Project01 要求固定 40/10 划分和 90 维体积特征，并建议按训练样本将每个特征标准化。Lab 2 的训练 TODO 没有提供已完成的模型代码；固定 RBF 核、C=1、gamma='scale' 和五折 CV 是本实现选择，不是老师规定的“最佳参数”。五折 CV 用于估计固定模型在训练集内的表现，不进行调参。

PDF 的结果表正文要求 Data_40～49，例表第一行误写为 Data_30；本代码按明确的测试划分输出 Data_40～49。

## 关键处理

1. `data_labels.csv` 的 New Name 有空格和 `.nii` 后缀；读取时规范化为 Data_XX，再按编号匹配。不能按 CSV 行位置拼接。
2. 特征只包含 ROI_1_mm3～ROI_90_mm3，按数值编号排列。FileName、Original Name 和标签不作为特征。
3. NC=0、AD=1。StandardScaler 只在训练数据上拟合；交叉验证每一折也独立拟合 scaler。
4. 测试标签仅用于已保存预测的最终评估，不参与标准化、训练、选特征或参数选择。
5. 体积未经 TIV 归一化；本代码进行的是按 ROI 的标准化。所有 10 名测试者均保留，包括采用已确认 BET 结果的 Data_44，其预处理质量限制仍应在报告中说明。

## 结果用途

`test_predictions.csv` 的 FileName / Prediction 两列就是项目报告的预测表。`test_evaluation.csv` 是与已提供标签的对照，不能把 TrueLabel 当作预测提交。`AD_decision_score` 为有符号 SVM 分数，不是概率。

`training_record.json` 保存软件版本、CV 分数、输入 SHA256、标签编码和 scaler 参数，便于复现。`svm_model.joblib` 保存模型和特征顺序；在与训练时相同的依赖版本中加载。这里只输出作业数据上的结果，没有证明某个参数组合最优或对其它数据的泛化性能。

参考：[SVC 官方文档](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)、[数据泄漏与 Pipeline](https://scikit-learn.org/stable/common_pitfalls.html)、[交叉验证](https://scikit-learn.org/stable/modules/cross_validation.html)。
