# Data Files Reference

This directory is a placeholder. All runtime data lives in `extracted/` (produced by
running `bash scripts/extract_data.sh` from the repository root).

> **Do not commit binary data to git.** Large files (`.fits`, `.npz`, `.npy`) are listed
> in `.gitignore`. Use the provided archive `files.7z` to distribute or transfer data.

---

## File Inventory

### Sky Maps (HEALPix FITS)

| File | nside | Pixels | Description |
|------|-------|--------|-------------|
| `density_map.fits` | 512 | 3,145,728 | Full-resolution galaxy density map (SDSS DR18 low-z) |
| `density_nside16.fits` | 16 | 3,072 | Degraded density map — primary analysis resolution |
| `density_nside32.fits` | 32 | 12,288 | Intermediate resolution |
| `density_nside8.fits` | 8 | 768 | Coarsest resolution used in analysis |
| `density_map_wide.fits` | 64 | 49,152 | Wide-z galaxy sample density map |
| `density_map_nside64.fits` | 64 | 49,152 | Standard resolution density map |
| `density_map_nside128.fits` | 128 | 196,608 | High-resolution density map |
| `cluster_map.fits` | 512 | 3,145,728 | Full-resolution cluster richness sum map |
| `cluster_count_nside16.fits` | 16 | 3,072 | Cluster *count* per pixel at nside=16 (primary Y variable) |
| `cluster_count_nside32.fits` | 32 | 12,288 | Cluster count at nside=32 |
| `cluster_count_nside8.fits` | 8 | 768 | Cluster count at nside=8 |
| `cluster_map_nside64.fits` | 64 | 49,152 | Cluster count at nside=64 |
| `ricci_map_nside16.fits` | 16 | 3,072 | Discrete Ollivier–Ricci curvature κ per pixel |

**HEALPix convention:** All maps use the RING ordering scheme and Galactic coordinates.
Masked / invalid pixels are set to `healpy.UNSEEN` (-1.6375e+30).

**How density maps are built:**
```
n_galaxies_pixel / mean(n_galaxies_nonzero_pixels)
```
This normalises by the mean occupation so that the map represents relative over/under-density.

**How cluster maps are built:**
Either the sum of richness λ per pixel (early approach) or the raw count of cluster centres
per pixel (final approach). The count approach reduces sparsity at nside≤16.

---

### Galaxy & Cluster Catalogs (FITS tables)

| File | Rows | Columns (key) | Source |
|------|------|---------------|--------|
| `large_sample.fits` | 75,770 | `ra, dec, z, class, zwarning, u, g, r, i, photoz` | SDSS DR18 CasJobs spectroscopic query |
| `galaxies_wide.fits` *(not in archive)* | 752,693 | `ra, dec, z` | Extended redshift query z∈[0.05,0.60] |
| `cat_dr8.fits` *(not in archive)* | 26,111 | `ra, dec, z_lambda, lambda` | redMaPPer DR8 from VizieR |
| `redmapper_des_sva1.fits` | varies | `ra, dec, z_lambda, lambda` | DES SVA1 redMaPPer |
| `large_sample.fits` selection criteria | — | — | CLASS='GALAXY', ZWARNING=0, 0.0434≤z≤0.1175 |

**Reproducing `large_sample.fits`** — Run the following SQL in CasJobs (SDSS DR18 context):

```sql
SELECT
    s.ra, s.dec, s.z, s.class, s.zWarning,
    p.u, p.g, p.r, p.i,
    p.petroMag_r,
    s.z AS photoz
INTO mydb.large_sample
FROM SpecObj AS s
JOIN PhotoObj AS p ON s.bestObjID = p.objID
WHERE
    s.class = 'GALAXY'
    AND s.zWarning = 0
    AND s.z BETWEEN 0.0434 AND 0.1175
    AND p.r BETWEEN 14.0 AND 17.77
```

Then download as FITS via CasJobs → MyDB → Export.

---

### NumPy Arrays (.npz / .npy)

| File | Keys / Shape | Description |
|------|-------------|-------------|
| `fisher_results.npz` | `l (513,)`, `Cl (513,)`, `Nl (513,)`, `Fl (513,)`, `MI (scalar)` | Angular power spectrum and Fisher information. `MI` = I(X;T) = 82.93 nats |
| `eta_IB_nside8.npz` | `I_TY`, `I_XT`, `eta_IB` (scalars) | IB results at nside=8 |
| `eta_IB_nside16.npz` | same | IB results at nside=16 |
| `eta_IB_cosmic_lowres.npz` | same | IB results at nside=64 |
| `eta_IB_abundance.npz` | same | IB using abundance estimator |
| `eta_IB_wide.npz` | same | IB using wide-z sample |
| `eta_IB_count.npz` | same | IB using raw cluster count |
| `hyper_ib_ricci_results.npz` | `mi_unweighted`, `mi_ricci`, `eta_unweighted`, `eta_ricci`, `alpha` | Ricci-weighted mutual information |
| `hyper_ib_results.npz` | `mi_unweighted`, `mi_weighted`, `eta_unweighted`, `eta_weighted`, `alpha` | Geometry-weighted mutual information |
| `etf_scores_bootstrap.npy` | `(100,)` float64 | ETF scores from 100 bootstrap samples (70% data each) |
| `etf_score_full.npy` | scalar | ETF score on full dataset (0.2256) |
| `phi_tda.npy` | scalar | Topological persistence Φ_TDA (977.08) |
| `classification_3d.npy` | `(128, 128, 128)` int8 | T-Web classification: 0=void, 1=sheet, 2=filament, 3=knot |
| `potential_3d.npy` | `(128, 128, 128)` float32 | Gravitational potential on 3D grid |

---

### Text Result Files (.txt)

| File | Content |
|------|---------|
| `eta_IB_nside8.txt` | I(T;Y), I(X;T), η_IB, valid pixels at nside=8 |
| `eta_IB_nside16.txt` | Same at nside=16 |
| `eta_IB_cosmic_lowres.txt` | Same at nside=64 |
| `eta_IB_cosmic_nside128.txt` | Same at nside=128 (result: 0.0 nats — too sparse) |
| `eta_IB_abundance.txt` | sklearn kNN and histogram estimator comparison |
| `eta_IB_wide.txt` | Results using wide-z galaxy sample |
| `eta_IB_count.txt` | Results using raw cluster count Y variable |
| `etf_results.txt` | Φ_TDA, full ETF score, bootstrap statistics |

---

### PNG Outputs

All `.png` files are Matplotlib figures generated by the pipeline scripts.
They are included for fast display in the Gallery section and as static fallbacks
when interactive recomputation would be slow.

| File | Description |
|------|-------------|
| `density_map.png` | Full SDSS footprint density map (Mollweide) |
| `cluster_map.png` | Full redMaPPer cluster map (Mollweide) |
| `power_spectrum.png` | Angular power spectrum C_ℓ |
| `hyper_ib_ricci_results.png` | Ricci-weighted MI summary figure |
| `hyper_ib_scatter.png` | Curvature κ vs MI contribution scatter |
| `etf_correlation.png` | ETF feature-target correlation |
| `eta_IB_*_scatter.png` | T vs Y scatter at each resolution |
| `eta_IB_scatter_histogram.png` | Histogram-based estimator scatter |

---

## Generating Your Own Data

If you want to reproduce results end-to-end:

```
1. SDSS SQL query         → large_sample.fits           (CasJobs)
2. redMaPPer download     → cat_dr8.fits                (VizieR)
3. build_density_map.py   → density_map.fits            (nside=512)
4. create_maps_nside*.py  → density/cluster nside maps
5. degrade_maps.py        → lower-res maps
6. fisher_analysis.py     → fisher_results.npz
7. compute_eta_*.py       → eta_IB_*.npz + .txt
8. compute_ricci*.py      → ricci_map_nside16.fits
9. hyper_ib_cosmic.py     → hyper_ib_*.npz
10. tda_ripser.py          → phi_tda.npy
11. etf_correlation.py     → etf_*.npy, etf_results.txt
12. classify_cosmic_web.py → classification_3d.npy
```

All scripts are included in the `extracted/` folder and are documented with inline comments.
