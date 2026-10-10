# 虚拟机预处理：脚本和实际三维输出

50 人预处理、4500 个体积值和 SVM 已完成。本目录保存从虚拟机下载的最终结果，不是模拟数据。`output_manifest.json` 记录每个输出的字节数及 SHA-256；全部 698 个文件已与虚拟机核对。

## 目录

- `scripts/`：五个 Bash 文件及最终 `bet_parameters.csv`。前四个主脚本的 TODO 已完成；`CreateSeedMask` 保留老师原始内容。
- `Output/train/`：Data_00～Data_39 的最终输出。
- `Output/test/`：Data_40～Data_49 的最终输出。
- [报告效果图和证据](../report_evidence/README.md)：BET、组织分割、配准图片及日志。

## 如何运行

将 `scripts/` 中六个文件放在 Linux 项目根目录，根目录同时准备 `Data/train`、`Data/test` 和 `Packages`。`Packages` 应包含 `MNI152_T1_1mm_brain.nii.gz` 与 `aal.nii.gz`。原始 MRI、老师的资料和软件安装包仍使用原始作业材料。

```bash
cd /home/elec5622/Project01
BET_DRY_RUN=1 bash SkullStripping
bash SkullStripping
bash TissueSegmentation
bash Registration
bash Measurement
```

`Measurement` 自动调用 `CreateSeedMask`，不用单独运行。脚本默认 FSL 路径 `/home/elec5622/fsl`，NiftyReg 安装路径 `/home/elec5622/niftyreg/niftyreg_install`；可用 `FSLDIR`、`NIFTYREG_INSTALL` 和 `PROJECT_ROOT` 指定其它安装或项目目录。

以上命令会重新处理数据；本仓库提供的最终输出已处理完毕，可直接查看。SVM 在仓库根目录运行。

## 三维文件分别是什么

| 文件名（以 Data_00 为例） | 内容 |
| --- | --- |
| `Data_00_brain.nii.gz` | BET 去除颅骨及部分非脑组织后的脑图像 |
| `Data_00_brain_mask.nii.gz` | BET 二值脑掩膜 |
| `Data_00_csf_mask.nii.gz` | FAST 的脑脊液二值掩膜 |
| `Data_00_greymatter_mask.nii.gz` | FAST 的灰质二值掩膜，体积测量使用此文件 |
| `Data_00_whitematter_mask.nii.gz` | FAST 的白质二值掩膜 |
| `Data_00_brain_greymatter.nii.gz` | 脑图像乘灰质掩膜得到的灰质强度图 |
| `Data_00_brain_seg.nii.gz` | FAST 离散组织分类图 |
| `Data_00_brain_mixeltype.nii.gz` | FAST 的混合组织类别辅助输出 |
| `Data_00_MNI_to_native_affine.txt` | MNI 模板到个人空间的仿射变换 |
| `Data_00_MNI_to_native_cpp.nii.gz` | 非线性变换控制点文件，不能当作普通解剖脑图查看 |
| `Data_00_MNI_affine.nii.gz` | 仿射配准后的 MNI 模板 |
| `Data_00_MNI_warped.nii.gz` | 非线性配准后的 MNI 模板 |
| `AAL_to_Data_00.nii.gz` | 传播到个人空间的 AAL 图谱，最近邻插值保留区域编号 |
| `AAL_statistics_volumn_train.csv` | 40 人最终 90 维体积表；测试目录有对应 test 表 |
| `AAL_statistics_volumn_train_Data_XX.csv` | 并行测量时保存的单人中间 CSV；最终 CSV 为完整合并表 |

实际每人文件集合以清单为准。ROI 掩膜在测量时临时生成并清理，最终的个人 AAL 标签图保留完整区域定义，可重新生成这些掩膜。没有把 116 个临时 ROI 掩膜重复存进仓库。

## 如何查看

GitHub 可以预览 PNG；三维 `.nii.gz` 需要下载后用 FSLeyes 查看。例如：

```bash
fsleyes Output/train/Data_00_brain.nii.gz Output/train/AAL_to_Data_00.nii.gz
```

在 FSLeyes 中给 AAL 图层设置离散标签色图和透明度，再检查多个方向。可叠加灰质掩膜检查组织边界。报告中的三维配准是在个人空间：模板和图谱被变换到个人脑图，不要写成把所有个人 MRI 变换到 MNI 后测量。

## 结果限制

Data_44 保留此前确认的数据，仍有 BET 额部边界疑似遗漏及非脑组织残留问题。数值核对通过不代表解剖分割完全正确。没有用测试标签或 SVM 分数调整这些 BET 参数。
