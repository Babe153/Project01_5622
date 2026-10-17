"""Post hoc descriptive analysis of the 40 training subjects only.

This supplement does not train models, rank/select inputs, or read test features.
Run from the repository root with numpy, matplotlib and nibabel installed.
"""
from pathlib import Path
import csv
import hashlib
import json
import numpy as np
import nibabel as nib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    repo = Path(__file__).resolve().parents[2]
    paths = [repo / 'data/AAL_statistics_volumn_train.csv',
             repo / 'data/data_labels.csv',
             repo / 'submission/processing_qc_records.csv']
    dest = repo / 'report_evidence/training_analysis'
    dest.mkdir(exist_ok=True)
    with paths[0].open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    ids = [r['FileName'] for r in rows]
    assert ids == [f'Data_{i:02}' for i in range(40)]
    with paths[1].open(encoding='utf-8-sig', newline='') as f:
        labels = {r['New Name'].strip().removesuffix('.nii'): r['Label'].strip()
                  for r in csv.DictReader(f)}
    with paths[2].open(encoding='utf-8-sig', newline='') as f:
        qc = {r['subject_id']: r for r in csv.DictReader(f) if r['split'] == 'train'}
    x = np.array([[float(r[f'ROI_{i}_mm3']) for i in range(1, 91)] for r in rows])
    y = np.array([labels[i] == 'AD' for i in ids])
    assert x.shape == (40, 90) and y.sum() == 19 and np.all(x > 0)
    total = x.sum(axis=1)
    gm = np.array([float(qc[i]['gm_total_mm3']) for i in ids])
    assert np.allclose(total, [float(qc[i]['roi_1_90_sum_mm3']) for i in ids])
    fraction = x / total[:, None]
    assert np.allclose(fraction.sum(axis=1), 1)
    geometry = []
    for subject in ids:
        path = repo / 'preprocessing/Output/train' / f'{subject}_greymatter_mask.nii.gz'
        image = nib.load(path)
        geometry.append({'subject_id': subject, 'label': labels[subject],
                         'shape': list(image.shape),
                         'voxel_sizes_mm': [float(z) for z in image.header.get_zooms()[:3]],
                         'header_sha256': hashlib.sha256(image.header.binaryblock).hexdigest()})
    (dest/'training_geometry.json').write_text(json.dumps(geometry, indent=2)+'\n', encoding='utf-8')
    assert all(g['shape'] == [256,256,176] and g['voxel_sizes_mm'] == [1,1,1]
               for g in geometry if g['label']=='NC')
    assert all(g['shape'][:2] == [256,256] and g['shape'][2] in [166,170]
               and not np.allclose(g['voxel_sizes_mm'], [1,1,1])
               for g in geometry if g['label']=='AD')

    def summary(a):
        return {c: {'n': int(mask.sum()), 'mean': float(a[mask].mean()),
                    'sd': float(a[mask].std(ddof=1)), 'min': float(a[mask].min()),
                    'max': float(a[mask].max())}
                for c, mask in [('NC', ~y), ('AD', y)]}

    def effect(a):
        # Cohen's d, AD minus NC, with the sample-size-weighted pooled SD.
        pooled = np.sqrt(((y.sum()-1)*a[y].var(axis=0, ddof=1)
                          + ((~y).sum()-1)*a[~y].var(axis=0, ddof=1)) / (len(y)-2))
        assert np.all(pooled > 0)
        return (a[y].mean(axis=0)-a[~y].mean(axis=0)) / pooled

    d_abs, d_frac = effect(x), effect(fraction)
    record = {
        'purpose': 'Post hoc training-only description of global scale and regional composition',
        'subjects': ids, 'class_counts': {'NC': 21, 'AD': 19},
        'no_test_features_read': True, 'no_model_refitting_or_selection': True,
        'whole_binary_gm_mm3': summary(gm), 'aal_1_90_sum_mm3': summary(total),
        'aal_sum_AD_minus_NC_percent_of_NC_mean': float((total[y].mean()/total[~y].mean()-1)*100),
        'absolute_negative_d_count': int((d_abs < 0).sum()),
        'fraction_negative_d_count': int((d_frac < 0).sum()),
        'median_absolute_d_raw': float(np.median(abs(d_abs))),
        'median_absolute_d_fraction': float(np.median(abs(d_frac))),
        'absolute_fraction_sign_change_count': int((np.sign(d_abs) != np.sign(d_frac)).sum()),
        'training_geometry': {
            'NC': 'All 21: 256 x 256 x 176; voxel sizes 1 x 1 x 1 mm',
            'AD': 'All 19: 256 x 256 x 166 or 170; non-isotropic voxel sizes',
            'AD_voxel_size_ranges_mm': [[min(g['voxel_sizes_mm'][axis] for g in geometry if g['label']=='AD'),
                                         max(g['voxel_sizes_mm'][axis] for g in geometry if g['label']=='AD')]
                                        for axis in range(3)],
            'interpretation': 'Class-associated stored geometry; scanner/site provenance unavailable'},
        'pooled_sd_formula': 'sqrt(((n_AD-1)*s_AD^2+(n_NC-1)*s_NC^2)/(n_AD+n_NC-2))',
        'effect_definition': '(mean_AD - mean_NC) / pooled_sample_SD',
        'fraction_definition': 'ROI_volume / sum_of_ROI_1_to_90_volumes_for_that_subject',
        'limitations': ['Post hoc descriptive analysis; no inferential tests or causal claims',
                        'Fractions are not intracranial-volume adjustment and are compositional',
                        'Group effect sizes are not SVM feature importance or predictive performance',
                        'GM totals share the original segmentation and BET limitations'],
        'input_sha256': {str(p.relative_to(repo)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in paths}}
    (dest/'summary.json').write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
    with (dest/'subject_summaries.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['subject_id', 'label', 'whole_binary_gm_mm3', 'aal_1_90_sum_mm3'])
        writer.writerows(zip(ids, ['AD' if v else 'NC' for v in y], gm, total))
    with (dest/'regional_effects.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['aal_label', 'd_absolute_volume_AD_minus_NC', 'd_fraction_AD_minus_NC'])
        writer.writerows(zip(range(1,91), d_abs, d_frac))

    plt.rcParams.update({'font.family': 'Times New Roman', 'font.size': 11,
                         'svg.fonttype': 'none'})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.15), gridspec_kw={'width_ratios':[.8,1.65]})
    ax = axes[0]
    for pos, mask, marker in [(0, ~y, 'o'), (1, y, '^')]:
        values = total[mask]/1000
        # Deterministic jitter by subject order; every point is one subject.
        jitter = np.linspace(-.15,.15,len(values))
        ax.scatter(pos+jitter, values, s=28, marker=marker, facecolors='white', edgecolors='black', lw=.8)
        ax.plot([pos-.22,pos+.22], [values.mean()]*2, color='black', lw=2)
    ax.set_xticks([0,1], ['NC (n = 21)', 'AD (n = 19)'])
    ax.set_ylabel('Sum of AAL 1–90 GM volumes (cm³)')
    ax.set_title('(a) Overall regional GM scale', loc='left', fontweight='bold', fontsize=12)
    ax.set_xlim(-.45,1.45)
    ax = axes[1]
    ax.plot(np.arange(1,91), d_abs, 'o-', color='black', markersize=2.6, linewidth=.8,
            label='Absolute volume')
    ax.plot(np.arange(1,91), d_frac, '^--', color='.5', markersize=2.6, linewidth=.8,
            label='Fraction of AAL 1–90 sum')
    ax.axhline(0, color='black', lw=.7)
    ax.set_xlabel('AAL label (original order; all 90 shown)')
    ax.set_ylabel('Descriptive Cohen’s d (AD − NC)')
    ax.set_xlim(0,91)
    ax.set_title('(b) Sensitivity to volume representation', loc='left', fontweight='bold', fontsize=12)
    ax.legend(loc='upper left', fontsize=10, frameon=False)
    for ax in axes:
        ax.spines[['top','right']].set_visible(False)
        ax.tick_params(direction='out')
        ax.grid(axis='y', color='.88', linewidth=.45)
        ax.set_axisbelow(True)
    fig.tight_layout(w_pad=2)
    fig.savefig(dest/'training_volume_sensitivity.png', dpi=350, bbox_inches='tight', facecolor='white')
    svg=dest/'training_volume_sensitivity.svg'
    fig.savefig(svg, bbox_inches='tight', facecolor='white')
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)
    print(json.dumps({k:v for k,v in record.items() if k not in ['subjects','input_sha256','limitations']}, indent=2))


if __name__ == '__main__':
    main()
