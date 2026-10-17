"""Render Figure 2 from the existing Data_00 NIfTI outputs.

Run from any directory with Python, numpy, nibabel, and matplotlib installed.
This utility reads the completed preprocessing outputs; it does not rerun FSL.
"""
from pathlib import Path
import csv
import hashlib
import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import nibabel as nib
import numpy as np


def main():
    repo = Path(__file__).resolve().parents[2]
    base = repo / 'preprocessing/Output/train'
    dest = repo / 'report_evidence/figures'
    names = ['Data_00_brain.nii.gz', 'AAL_to_Data_00.nii.gz',
             'Data_00_greymatter_mask.nii.gz']
    native = [nib.load(base / name) for name in names]
    brain_image, atlas_image, gm_image = native
    assert all(i.shape == brain_image.shape for i in native)
    assert all(np.allclose(i.affine, brain_image.affine) for i in native)
    assert gm_image.header.get_xyzt_units()[0] == 'mm'
    atlas = atlas_image.get_fdata(dtype=np.float32)
    gm = gm_image.get_fdata(dtype=np.float32)
    assert np.isin(gm, [0, 1]).all()
    assert np.allclose(atlas, np.rint(atlas))
    roi = atlas == 1
    intersection = roi & (gm > 0)
    count = int(np.count_nonzero(intersection))
    zooms = [float(v) for v in gm_image.header.get_zooms()[:3]]
    voxel_volume = float(np.prod(zooms, dtype=np.float64))
    volume = count * voxel_volume
    csv_path = repo / 'data/AAL_statistics_volumn_train.csv'
    with csv_path.open(newline='', encoding='utf-8-sig') as stream:
        row = next(r for r in csv.DictReader(stream) if r['FileName'] == 'Data_00')
    stored = float(row['ROI_1_mm3'])
    assert abs(volume - stored) < 1e-6

    # Reorientation changes the view only. Counts above use the native grid.
    brain, aal, gm_view = [nib.as_closest_canonical(i).get_fdata(dtype=np.float32) for i in native]
    roi_view = aal == 1
    intersect_view = roi_view & (gm_view > 0)
    z = int(np.argmax(intersect_view.sum(axis=(0, 1))))
    foreground = np.argwhere(brain[:, :, z] > 0)
    lo = np.maximum(foreground.min(axis=0) - 6, 0)
    hi = np.minimum(foreground.max(axis=0) + 7, brain.shape[:2])
    crop = (slice(lo[0], hi[0]), slice(lo[1], hi[1]), z)
    voxel_sizes = nib.as_closest_canonical(brain_image).header.get_zooms()
    aspect = float(voxel_sizes[1] / voxel_sizes[0])

    plt.rcParams.update({'font.family': 'Times New Roman', 'svg.fonttype': 'none'})
    fig = plt.figure(figsize=(13, 7.9), facecolor='white')
    overlay = fig.add_axes([0, 0, 1, 1], zorder=5)
    overlay.set_xlim(0, 1); overlay.set_ylim(0, 1); overlay.axis('off')
    overlay.text(.5, .967, 'Data_00  |  AAL label 1  |  Native-space volume extraction',
                 ha='center', va='center', fontsize=21, weight='bold')
    boxes = [[.025, .425, .285, .43], [.3575, .425, .285, .43], [.69, .425, .285, .43]]
    titles = ['(a)  ROI localisation', '(b)  Binary ROI mask', '(c)  Regional GM mask']
    subtitles = ['AAL label 1 outlined on native MRI', 'ROI 1 = 1; all other voxels = 0',
                 'ROI 1 intersected with binary GM']
    vmax = float(np.percentile(brain[brain > 0], 99))
    for i, rect in enumerate(boxes):
        ax = fig.add_axes(rect)
        ax.set_facecolor('black')
        if i == 0:
            ax.imshow(brain[crop].T, origin='lower', cmap='gray', vmin=0, vmax=vmax, aspect=aspect)
            ax.contour(roi_view[crop].T, levels=[.5], colors='white', linewidths=1.3)
        else:
            data = roi_view if i == 1 else intersect_view
            ax.imshow(data[crop].T, origin='lower', cmap='gray', vmin=0, vmax=1,
                      interpolation='nearest', aspect=aspect)
        ax.set_xticks([]); ax.set_yticks([])
        for spine in ax.spines.values(): spine.set_linewidth(.8)
        overlay.text(rect[0] + rect[2] / 2, .89, titles[i], ha='center', fontsize=19, weight='bold')
        overlay.text(rect[0] + rect[2] / 2, .386, subtitles[i], ha='center', fontsize=16)
    for start, end in [(.316, .351), (.648, .683)]:
        overlay.add_patch(FancyArrowPatch((start, .64), (end, .64), arrowstyle='-|>',
                                         mutation_scale=20, color='black', lw=1.4))
    overlay.text(.025, .309, '(d)  Count the complete 3D intersection and write one feature',
                 fontsize=19, weight='bold')
    overlay.text(.025, .249, f'GM voxel count in ROI 1:  {count:,}', fontsize=18)
    overlay.text(.025, .197, f'One voxel:  {voxel_volume:.9f} mm³', fontsize=18)
    overlay.text(.025, .137, f'Volume:  {count:,} × {voxel_volume:.9f}', fontsize=18)
    overlay.text(.025, .084, f'              ≈ {volume:,.6f} mm³', fontsize=18, weight='bold')
    table_ax = fig.add_axes([.515, .115, .46, .16]); table_ax.axis('off')
    cells = [['Data_00', f"{float(row['ROI_1_mm3']):.2f}",
              f"{float(row['ROI_2_mm3']):.2f}", '…', f"{float(row['ROI_90_mm3']):.2f}"]]
    table = table_ax.table(cellText=cells, colLabels=['Subject', 'ROI 1', 'ROI 2', '…', 'ROI 90'],
                           colWidths=[.24, .22, .22, .08, .24], cellLoc='center', loc='center')
    table.auto_set_font_size(False); table.set_fontsize(15); table.scale(1, 2.0)
    for (r, c), cell in table.get_celld().items():
        cell.set_facecolor('white'); cell.set_edgecolor('black'); cell.set_linewidth(.7)
        if r == 0: cell.set_text_props(weight='bold')
    overlay.text(.745, .097, 'Repeat for labels 1–90 → 90 volumes per subject', ha='center', fontsize=16)
    overlay.text(.745, .056, 'Feature-table values shown rounded to two decimals.', ha='center', fontsize=14)
    overlay.text(.5, .014, 'Panels (a–c) show one axial slice. The volume in (d) uses all slices, not just this image.',
                 ha='center', fontsize=15)
    for extension in ['png', 'svg']:
        output = dest / f'roi_volume_extraction_Data_00.{extension}'
        fig.savefig(output, dpi=350, facecolor='white')
        if extension == 'svg':
            output.write_text('\n'.join(line.rstrip() for line in output.read_text(encoding='utf-8').splitlines()) + '\n', encoding='utf-8', newline='\n')
    plt.close(fig)
    record = {
        'subject': 'Data_00', 'aal_label': 1,
        'input_files': [{'path': str((base / name).relative_to(repo)).replace('\\', '/'),
                         'sha256': hashlib.sha256((base / name).read_bytes()).hexdigest()} for name in names],
        'feature_csv': str(csv_path.relative_to(repo)).replace('\\', '/'),
        'native_voxel_dimensions_mm': zooms, 'native_voxel_volume_mm3': voxel_volume,
        'roi_voxel_count': int(roi.sum()), 'gm_roi_voxel_count': count,
        'calculated_gm_volume_mm3': volume, 'csv_gm_volume_mm3': stored,
        'absolute_difference_mm3': abs(volume - stored),
        'display_orientation': 'canonical RAS; display reorientation only',
        'canonical_axial_slice_index_zero_based': z,
        'measurement_scope': 'complete 3D masks; not the displayed slice',
    }
    (dest / 'roi_volume_extraction_Data_00.json').write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(record, indent=2))


if __name__ == '__main__':
    main()
