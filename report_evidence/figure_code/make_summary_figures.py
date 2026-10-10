"""Create report figures from the saved training record and implemented pipeline."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.ticker import PercentFormatter

HERE=Path(__file__).resolve().parent.parent
REPO=HERE.parent
OUT=HERE/'figures'
OUT.mkdir(exist_ok=True)
record=json.loads((REPO/'results/training_record.json').read_text(encoding='utf-8'))
cv=record['training_cv']
scores=cv['fold_accuracy']
fig,ax=plt.subplots(figsize=(8,4.8),layout='constrained')
bars=ax.bar(range(1,6),scores,color='#287f9d',width=.6)
ax.axhline(cv['mean_accuracy'],color='#c06a19',linestyle='--',linewidth=1.8,label=f"Mean: {cv['mean_accuracy']:.1%}")
ax.bar_label(bars,labels=[f'{v:.1%}' for v in scores],padding=5,fontsize=11)
ax.set(xticks=range(1,6),xlabel='Stratified training fold',ylabel='Accuracy',ylim=(0,1.13),title='Training-only 5-fold cross-validation (40 subjects)')
ax.yaxis.set_major_formatter(PercentFormatter(1))
ax.set_yticks([0,.25,.5,.75,1])
ax.spines[['top','right']].set_visible(False)
ax.legend(loc='lower right',frameon=False)
fig.supxlabel('StandardScaler + RBF SVC; scaler fitted inside each fold',fontsize=9,color='#475569')
fig.savefig(OUT/'training_cv_accuracy.png',dpi=200)
plt.close(fig)

fig,ax=plt.subplots(figsize=(12,10))
ax.set(xlim=(0,12),ylim=(0,10))
ax.axis('off')
def box(x,y,w,h,title,body,color='#e5f0f5'):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.06,rounding_size=0.12',facecolor=color,edgecolor='#30758b',linewidth=1.3))
 ax.text(x+w/2,y+h*.7,title,ha='center',va='center',fontsize=13,fontweight='bold',color='#153b4b')
 ax.text(x+w/2,y+h*.28,body,ha='center',va='center',fontsize=10,color='#244b5c')
def arrow(a,b):
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.7,'color':'#3b6577'})
ax.text(6,9.7,'Project01: implemented MRI-to-SVM workflow',ha='center',fontsize=18,fontweight='bold',color='#153b4b')
stages=[
 ('T1 MRI: 50 subjects','Fixed split: 40 training + 10 test'),
 ('BET skull stripping','Per-subject f, g and optional centre from bet_parameters.csv'),
 ('FAST tissue segmentation','Binary GM / WM / CSF masks; brain image x GM mask'),
 ('Template and AAL registration','MNI -> native affine + nonlinear; AAL nearest-neighbour labels'),
 ('90 regional GM volumes','AAL labels 1-90 intersect binary GM; physical volume in mm3'),
]
for i,(title,body) in enumerate(stages):
 y=8.3-i*1.25
 box(1.2,y,9.6,.95,title,body)
 if i:arrow((6,y+1.25),(6,y+.97))
box(.5,1.15,5.2,1.3,'Training: 40 subjects','StandardScaler + RBF SVC (C=1, gamma=scale)\n5-fold CV; then fit on all 40',color='#e3f2e9')
box(6.4,1.15,5.1,1.3,'Prediction: 10 test subjects','Apply fitted scaler and SVM\nSave predictions before test-label evaluation')
arrow((4.2,3.3),(3.1,2.48))
arrow((7.8,3.3),(8.95,2.48))
arrow((5.76,1.8),(6.33,1.8))
ax.text(6,2.04,'fitted\nmodel',ha='center',fontsize=8,color='#475569')
arrow((8.95,1.1),(8.95,.72))
ax.text(8.95,.48,'Evaluation: compare with provided test labels\n9/10 correct (90%); Data_49: AD -> NC',ha='center',va='center',fontsize=10,color='#153b4b')
ax.text(.5,.35,'VM: preprocessing\nLocal Python: SVM',ha='left',fontsize=10,color='#475569')
fig.savefig(OUT/'pipeline_overview.png',dpi=200,bbox_inches='tight',facecolor='white')
plt.close(fig)
print('REPORT_FIGURES_CREATED_FROM_ACTUAL_TRAINING_RECORD')
