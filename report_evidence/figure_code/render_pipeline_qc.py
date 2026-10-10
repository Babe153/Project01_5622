from pathlib import Path
import json,os
import nibabel as nib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path('/home/elec5622/Project01');area=root/'Validation/final_pipeline_20261009';qc=area/'qc';qc.mkdir(exist_ok=True)
state=json.loads((area/'status.json').read_text())
only=os.environ.get('QC_SUBJECT')
complete=[d for d in state['subjects'] if d['stages'].get('Registration',{}).get('status')=='complete' and (not only or d['subject']==only)]
for d in complete:
    s=d['subject'];out=root/'Output'/d['split'];base=out/s
    if (qc/(s+'.json')).exists():continue
    brainimg=nib.as_closest_canonical(nib.load(str(base)+'_brain.nii.gz'))
    brain=brainimg.get_fdata(dtype=np.float32);zoom=brainimg.header.get_zooms()
    images={}
    for name,suffix in [('gm','_greymatter_mask.nii.gz'),('wm','_whitematter_mask.nii.gz'),('csf','_csf_mask.nii.gz'),('affine','_MNI_affine.nii.gz'),('warped','_MNI_warped.nii.gz')]:
        images[name]=nib.as_closest_canonical(nib.load(str(base)+suffix)).get_fdata(dtype=np.float32)
    atlas=nib.as_closest_canonical(nib.load(str(out/f'AAL_to_{s}.nii.gz'))).get_fdata(dtype=np.float32)
    mask=nib.as_closest_canonical(nib.load(str(base)+'_brain_mask.nii.gz')).get_fdata(dtype=np.float32)>0
    pos=np.where(mask);lo=[p.min() for p in pos];hi=[p.max() for p in pos]
    cuts=[(a,int(round(lo[a]+(hi[a]-lo[a])*f))) for a in range(3) for f in [.28,.5,.72]]
    vmax=np.percentile(brain[brain>0],99)
    def panel(ax,data,axis,index,overlay=None,color=None):
        z=[zoom[k] for k in range(3) if k!=axis]
        ax.imshow(np.take(data,index,axis=axis).T,origin='lower',cmap='gray',vmin=0,vmax=vmax,aspect=z[1]/z[0])
        if overlay is not None:
            cut=np.take(overlay,index,axis=axis).T
            if color and cut.any() and not cut.all():ax.contour(cut,levels=[.5],colors=[color],linewidths=.55)
            elif not color:ax.imshow(np.ma.masked_where(cut==0,cut),origin='lower',cmap='nipy_spectral',vmin=1,vmax=116,alpha=.40,aspect=z[1]/z[0],interpolation='nearest')
        ax.set_xticks([]);ax.set_yticks([])
    for mode in ['tissue','registration']:
        fig,axes=plt.subplots(3,9,figsize=(18,8.5))
        for col,(axis,index) in enumerate(cuts):
            if mode=='tissue':
                for row,(name,color) in enumerate([('gm','#ff4444'),('wm','#00d4ff'),('csf','#ffe600')]):panel(axes[row,col],brain,axis,index,images[name],color)
            else:
                for row,name in enumerate(['affine','warped']):
                    panel(axes[row,col],brain,axis,index,images[name]>np.percentile(images[name][images[name]>0],5),'#ff4444')
                    # Overlay warped intensity to expose internal alignment as well as outline.
                    cut=np.take(images[name],index,axis=axis).T
                    z=[zoom[k] for k in range(3) if k!=axis]
                    axes[row,col].imshow(np.ma.masked_where(cut<=0,cut),origin='lower',cmap='cool',vmin=0,vmax=np.percentile(images[name][images[name]>0],99),alpha=.35,aspect=z[1]/z[0])
                panel(axes[2,col],brain,axis,index,atlas)
            axes[0,col].set_title(['Sag','Cor','Axi'][axis]+f' #{index}',fontsize=9)
        for row,label in enumerate(['GM (red)','WM (cyan)','CSF (yellow)'] if mode=='tissue' else ['Affine MNI overlay','Nonlinear MNI overlay','AAL discrete labels']):axes[row,0].set_ylabel(label,fontsize=10)
        fig.suptitle(s+' | '+mode+' | native anatomy displayed in RAS',fontsize=13)
        fig.tight_layout(rect=[0,0,1,.96],pad=.4,h_pad=1,w_pad=.1)
        fig.savefig(str(qc/f'{s}_{mode}.png'),dpi=140);plt.close(fig)
    (qc/(s+'.json')).write_text(json.dumps({'subject':s,'split':d['split'],'slices_ras':cuts,'stage_validation':d['stages']},indent=2))
    print('PIPELINE_QC_READY',s,flush=True)
