"""Draw the implemented workflow for the English and Chinese home READMEs."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.font_manager import FontProperties

BASE=Path(__file__).resolve().parent.parent
BLUE='#246b91'
GREEN='#26765b'
INK='#193549'

TEXT={
 'en':{
  'title':'Project01: from brain MRI to AD / NC predictions',
  'subtitle':'What each step does, where it runs, and what it produces',
  'input':('INPUT: 50 T1 MRI scans','Training: Data_00–39 (40)  |  Test: Data_40–49 (10)'),
  'vm':'PART A · LINUX VM · FSL + NiftyReg',
  'local':'PART B · LOCAL COMPUTER / VSCODE · Python + scikit-learn',
  'steps':[
   ('1  Extract the brain (BET)','Remove skull and other non-brain tissue.','Brain image + binary brain mask','SkullStripping'),
   ('2  Separate brain tissues (FAST)','Classify grey matter, white matter, and CSF.','Binary GM / WM / CSF masks + GM intensity image','TissueSegmentation'),
   ('3  Locate anatomical regions (registration)','Map MNI template and AAL atlas to each native brain.\nAffine → nonlinear; nearest-neighbour atlas labels.','AAL region labels in the subject’s own MRI space','Registration'),
   ('4  Measure 90 regional GM volumes','For AAL regions 1–90, count GM-mask voxels × voxel volume.\nMeasurement calls CreateSeedMask automatically.','40-row train CSV + 10-row test CSV; 90 volumes/person (mm³)','Measurement'),
   ('5  Build feature matrices and training labels','Read ROI columns in order; match subject IDs to labels.\nNC = 0, AD = 1. IDs and labels are excluded from features.','X_train: 40 × 90; y_train: 40; X_test: 10 × 90','Project01_SVM.ipynb / project01_svm.py'),
   ('6  Validate and fit the classifier','StandardScaler + RBF SVM (C=1, gamma=scale).\n5-fold CV fits each training fold; refit on all 40 afterwards.','Fitted scaler + SVM model; training-only CV record','TRAINING DATA ONLY'),
   ('7  Predict the 10 test subjects','Apply the fitted scaler and SVM to the test volume matrix.\nSave predictions before comparing test labels.','test_predictions.csv: AD / NC for Data_40–49','NO REFITTING ON TEST DATA'),
   ('8  Evaluate saved predictions','Compare predictions with the supplied test labels.','Accuracy + sensitivity/specificity + confusion matrix','TEST LABELS ENTER HERE'),
  ],
  'params':('BET parameters','bet_parameters.csv\nf, g, optional centre'),
  'atlas':('Course templates','MNI brain template\n+ AAL atlas'),
  'trainlabels':('Training labels','data_labels.csv\nData_00–39 only'),
  'testlabels':('Test labels','data_labels.csv\nData_40–49 only'),
  'outtitle':'DELIVERABLES',
  'outputs':'Volume workbook: 50 subjects × 90 ROIs\nReport: methods + figures + predictions + results + limitations',
  'key':'The SVM learns from 90 numbers per person. Test labels are used only for final evaluation.',
 },
 'zh-CN':{
  'title':'Project01：从脑 MRI 到 AD / NC 分类',
  'subtitle':'每一步做什么、在哪里运行、得到什么结果',
  'input':('输入：50 人的 T1 脑 MRI','训练：Data_00–39（40 人）  |  测试：Data_40–49（10 人）'),
  'vm':'A 部分 · Linux 虚拟机 · FSL + NiftyReg',
  'local':'B 部分 · 本地电脑 / VSCode · Python + scikit-learn',
  'steps':[
   ('1  提取大脑（BET）','去除颅骨和其他非脑组织。','脑部图像 + 二值脑掩膜','SkullStripping'),
   ('2  区分脑组织（FAST）','将脑组织分为灰质、白质和脑脊液。','GM / WM / CSF 二值掩膜 + 灰质强度图','TissueSegmentation'),
   ('3  找到每人的脑区位置（配准）','将 MNI 模板及 AAL 图谱变换到个人脑图。\n先仿射、再非线性；AAL 用最近邻插值。','个人 MRI 空间中的 AAL 脑区标签图','Registration'),
   ('4  测量 90 个脑区的灰质体积','逐区计算：AAL 1–90 内的灰质体素数 × 每体素体积。\nMeasurement 会自动调用 CreateSeedMask。','训练 CSV 40 行 + 测试 CSV 10 行；每人 90 个体积（mm³）','Measurement'),
   ('5  整理特征矩阵及训练标签','按脑区编号读入体积，并按受试者 ID 匹配标签。\nNC = 0，AD = 1；ID 和标签不进入特征矩阵。','X_train：40 × 90；y_train：40；X_test：10 × 90','Project01_SVM.ipynb / project01_svm.py'),
   ('6  验证并训练分类模型','StandardScaler 标准化 + RBF SVM（C=1，gamma=scale）。\n五折验证在每折训练数据中拟合，最后用全部 40 人重训。','训练好的标准化器 + SVM 模型；训练内交叉验证记录','只使用训练数据'),
   ('7  预测 10 名测试者','用训练好的标准化器和 SVM 处理测试体积矩阵。\n先保存预测，再对照测试标签。','test_predictions.csv：Data_40–49 的 AD / NC 预测','测试时不重新拟合模型'),
   ('8  评估预测结果','将已保存的预测与老师提供的测试标签比较。','准确率 + 敏感度 / 特异度 + 混淆矩阵','测试标签只在这里用于评估'),
  ],
  'params':('逐人 BET 参数','bet_parameters.csv\nf、g、可选中心点'),
  'atlas':('老师提供的模板','MNI 脑模板\n+ AAL 标准脑区图谱'),
  'trainlabels':('训练者标签','data_labels.csv\n仅 Data_00–39'),
  'testlabels':('测试者标签','data_labels.csv\n仅 Data_40–49'),
  'outtitle':'最终交付',
  'outputs':'体积 Excel：50 人 × 90 个脑区\n报告：方法、效果图、逐人预测、结果及局限',
  'key':'SVM 从每人 90 个体积数值中学习。测试标签仅用于最后评估。',
 },
}

def draw(lang,font_path=None):
 t=TEXT[lang]
 font=FontProperties(fname=str(font_path)) if font_path else FontProperties(family='DejaVu Sans')
 fig,ax=plt.subplots(figsize=(14,19))
 fig.subplots_adjust(left=.015,right=.985,bottom=.015,top=.985)
 ax.set(xlim=(0,100),ylim=(0,151));ax.axis('off')
 def text(x,y,value,size=11,color=INK,weight='normal',ha='center'):
  ax.text(x,y,value,fontsize=size,color=color,fontproperties=font,fontweight=weight,ha=ha,va='center',linespacing=1.5)
 def panel(x,y,w,h,fill,edge):
  ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.3,rounding_size=1',facecolor=fill,edgecolor=edge,linewidth=1.2))
 def arrow(x1,y1,x2,y2,color=INK,dashed=False):
  ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'-|>','lw':1.6,'color':color,'linestyle':'--' if dashed else '-'})
 text(50,147,t['title'],size=20,weight='bold')
 text(50,143.3,t['subtitle'],size=11,color='#526679')
 panel(31,129.4,67,8,'#f0f3f7','#8096a6')
 text(64.5,134.8,t['input'][0],size=14,weight='bold')
 text(64.5,131.9,t['input'][1],size=10.5)

 panel(29.7,74.5,69.5,51,'#eaf3fa','#c4dbea')
 panel(29.7,15.1,69.5,55.4,'#edf6f0','#c6dfd0')
 text(32,123.2,t['vm'],size=11,color=BLUE,weight='bold',ha='left')
 text(32,68.3,t['local'],size=10.8,color=GREEN,weight='bold',ha='left')
 ys=[110.8,99.1,87.4,75.7,54.2,41.8,29.4,17.0]
 h=10.1
 for i,((title,body,output,script),y) in enumerate(zip(t['steps'],ys)):
  colour=BLUE if i<4 else GREEN
  panel(32,y,65,h,'white',colour)
  text(34,y+8.35,title,size=13.1,color=colour,weight='bold',ha='left')
  text(64.5,y+5.05,body,size=10.45)
  text(64.5,y+2.35,('Output: ' if lang=='en' else '输出：')+output,size=10.1,color=INK,weight='bold')
  text(64.5,y+.6,script,size=8.35,color='#5c7180')
  if i==4:
   # Route the VM-to-local connector around the local section heading.
   ax.plot([64.5,64.5,98.4,98.4,64.5],[75.4,72.9,72.9,65.1,65.1],color=INK,linewidth=1.6)
   arrow(64.5,65.1,64.5,y+h+.15)
  elif i:arrow(64.5,ys[i-1]-.25,64.5,y+h+.35)
 arrow(64.5,129.1,64.5,121.25)

 def side(key,y,colour):
  title,body=t[key];panel(1.5,y+1.4,25,7.4,'#fff9ed','#d9b776')
  text(14,y+6.9,title,size=10.4,color='#855b1e',weight='bold')
  text(14,y+3.7,body,size=9.6)
  arrow(26.8,y+5.05,31.5,y+5.05,colour,dashed=True)
 side('params',ys[0],BLUE)
 side('atlas',ys[2],BLUE)
 side('trainlabels',ys[4],GREEN)
 side('testlabels',ys[7],GREEN)
 # Keep the two label uses visually separate to show the fitting/evaluation boundary.
 panel(31,2.1,67,9.3,'#fff6e8','#ceaa6f')
 text(64.5,9.35,t['outtitle'],size=13,color='#855b1e',weight='bold')
 text(64.5,5.45,t['outputs'],size=10.9)
 arrow(64.5,16.6,64.5,11.7)
 text(1.5,73.3,'50 MRI → 50 × 90\nregional volumes' if lang=='en' else '50 人 MRI →\n50 × 90 个体积',size=11.2,color=BLUE,weight='bold',ha='left')
 text(1.5,42.9,'AD = Alzheimer’s disease\nNC = normal control' if lang=='en' else 'AD = 阿尔茨海默病\nNC = 正常对照',size=10.2,color=GREEN,ha='left')
 text(1.5,8.0,'PNG previews and QC notes\nare in report_evidence/' if lang=='en' else '效果图及检查记录：\nreport_evidence/',size=9.7,color='#526679',ha='left')
 text(50,.5,t['key'],size=10.3,color=INK)
 target=BASE/'figures'/f'project_workflow_{lang}.png'
 fig.savefig(target,dpi=180,facecolor='white')
 plt.close(fig)
 print(target.name)

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--chinese-font',type=Path,help='A font with Chinese glyphs, such as Microsoft YaHei or Noto Sans CJK.')
 args=parser.parse_args()
 draw('en')
 font_path=args.chinese_font or Path('C:/Windows/Fonts/msyh.ttc')
 if not font_path.is_file():parser.error('Supply --chinese-font to generate the Chinese figure.')
 draw('zh-CN',font_path)
