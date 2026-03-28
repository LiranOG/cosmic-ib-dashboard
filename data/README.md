# Data Files for Cosmic-Scale Information Bottleneck Dashboard

This folder is intentionally empty in the repository. Data files are too large for Git.

## Table of Contents

- [Quick Download](#quick-download)
- [File Inventory](#file-inventory)
  - [HEALPix Sky Maps](#healpix-sky-maps-fits)
  - [Galaxy and Cluster Catalogs](#galaxy-and-cluster-catalogs)
  - [NumPy Arrays](#numpy-arrays)
  - [Text Results](#text-result-files)
  - [PNG Outputs](#png-outputs)
- [Generating Your Own Data](#generating-your-own-data)
- [Troubleshooting](#troubleshooting)

---

## Quick Download

```bash
bash scripts/download_data.sh
```

Or manually:

1. Go to: https://github.com/LiranOG/cosmic-ib-dashboard/releases
2. Download the latest `files.7z`
3. Place it in the repository root
4. Run: `7z x files.7z -oextracted/`

**Archive integrity (SHA256):**

```bash
sha256sum files.7z          # Linux/macOS
certutil -hashfile files.7z SHA256   # Windows
```

> SHA256 checksum will be added here once the release is finalised.

**Expected file count after extraction:**

```bash
ls extracted/ | wc -l   # should print 105
```

---

## File Inventory

### HEALPix Sky Maps (FITS)

| File | nside | Pixels | Description |
|------|-------|--------|-------------|
| `density_map.fits` | 512 | 3,145,728 | Full-resolution galaxy density map (SDSS DR18 low-z) |
| `density_nside16.fits` | 16 | 3,072 | Degraded density map — primary analysis resolution |
| `density_nside32.fits` | 32 | 12,288 | Intermediate resolution |
| `density_nside8.fits` | 8 | 768 | Coarsest resolution |
| `density_map_nside64.fits` | 64 | 49,152 | Standard resolution density map |
| `density_map_nside128.fits` | 128 | 196,608 | High-resolution density map |
| `density_map_wide.fits` | 64 | 49,152 | Wide-z galaxy sample density map |
| `cluster_map.fits` | 512 | 3,145,728 | Full-resolution cluster richness sum map |
| `cluster_count_nside16.fits` | 16 | 3,072 | Cluster *count* per pixel — primary Y variable |
| `cluster_count_nside32.fits` | 32 | 12,288 | Cluster count at nside=32 |
| `cluster_count_nside8.fits` | 8 | 768 | Cluster count at nside=8 |
| `cluster_map_nside64.fits` | 64 | 49,152 | Cluster count at nside=64 |
| `ricci_map_nside16.fits` | 16 | 3,072 | Discrete Ollivier–Ricci curvature κ per pixel |

**HEALPix convention:** RING ordering, Galactic coordinates. Masked / invalid pixels are set to `healpy.UNSEEN` (−1.6375 × 10³⁰).

**Density map normalisation:**
```
density[i] = n_galaxies[i] / mean(n_galaxies[nonzero pixels])
```

### Galaxy and Cluster Catalogs

| File | Rows | Key columns | Source |
|------|------|-------------|--------|
| `large_sample.fits` | 75,770 | `ra, dec, z, class, zwarning, u, g, r, i` | SDSS DR18 CasJobs |
| `cat_dr8.fits` | 26,111 | `ra, dec, z_lambda, lambda` | redMaPPer DR8 (VizieR J/ApJS/785/104) |

**Reproducing `large_sample.fits`** — CasJobs SQL (DR18 context):

```sql
SELECT s.ra, s.dec, s.z, s.class, s.zWarning,
       p.u, p.g, p.r, p.i
INTO mydb.large_sample
FROM SpecObj AS s
JOIN PhotoObj AS p ON s.bestObjID = p.objID
WHERE s.class = 'GALAXY'
  AND s.zWarning = 0
  AND s.z BETWEEN 0.0434 AND 0.1175
  AND p.r BETWEEN 14.0 AND 17.77
```

### NumPy Arrays

| File | Keys / Shape | Description |
|------|-------------|-------------|
| `fisher_results.npz` | `MI` scalar, `l (513,)`, `Cl (513,)`, `Fl (513,)` | I(X;T)=82.93 nats, angular power spectrum |
| `eta_IB_nside8.npz` | `I_TY`, `I_XT`, `eta_IB` (scalars) | IB results at nside=8 |
| `eta_IB_nside16.npz` | same | IB results at nside=16 |
| `eta_IB_cosmic_lowres.npz` | same | IB results at nside=64 |
| `eta_IB_abundance.npz` | same | Abundance estimator results |
| `eta_IB_wide.npz` | same | Wide-z sample results |
| `eta_IB_count.npz` | same | Raw cluster count results |
| `hyper_ib_ricci_results.npz` | `mi_unweighted`, `mi_ricci`, `eta_unweighted`, `eta_ricci`, `alpha` | Ricci-weighted MI |
| `hyper_ib_results.npz` | `mi_unweighted`, `mi_weighted`, `eta_unweighted`, `eta_weighted`, `alpha` | Geometry-weighted MI |
| `etf_scores_bootstrap.npy` | `(100,)` float64 | ETF bootstrap scores |
| `etf_score_full.npy` | scalar | Full-sample ETF score (0.2256) |
| `phi_tda.npy` | scalar | Topological persistence Φ_TDA (977.08) |
| `classification_3d.npy` | `(128,128,128)` int8 | T-Web: 0=void, 1=sheet, 2=filament, 3=knot |
| `potential_3d.npy` | `(128,128,128)` float32 | Gravitational potential on 3D grid |

### Text Result Files

| File | Content |
|------|---------|
| `eta_IB_nside8.txt` | I(T;Y), I(X;T), η_IB, valid pixels at nside=8 |
| `eta_IB_nside16.txt` | Same at nside=16 |
| `eta_IB_cosmic_lowres.txt` | Same at nside=64 |
| `eta_IB_cosmic_nside128.txt` | Same at nside=128 (result: 0.0 — too sparse) |
| `eta_IB_abundance.txt` | sklearn kNN and histogram estimator comparison |
| `eta_IB_wide.txt` | Results using wide-z galaxy sample |
| `eta_IB_count.txt` | Results using raw cluster count Y variable |
| `etf_results.txt` | Φ_TDA, full ETF score, bootstrap statistics |

### PNG Outputs

| File | Description |
|------|-------------|
| `density_map.png` | Full SDSS footprint density map (Mollweide) |
| `cluster_map.png` | Full redMaPPer cluster map (Mollweide) |
| `power_spectrum.png` | Angular power spectrum C_ℓ |
| `hyper_ib_ricci_results.png` | Ricci-weighted MI summary figure |
| `hyper_ib_scatter.png` | Curvature κ vs MI contribution scatter |
| `etf_correlation.png` | ETF feature-target correlation |
| `eta_IB_*_scatter.png` | T vs Y scatter at each resolution |

---

## Generating Your Own Data

```
1.  SDSS SQL query          → large_sample.fits            (CasJobs)
2.  redMaPPer download      → cat_dr8.fits                 (VizieR)
3.  build_density_map.py    → density_map.fits             (nside=512)
4.  create_maps_nside*.py   → density / cluster nside maps
5.  degrade_maps.py         → lower-resolution maps
6.  fisher_analysis.py      → fisher_results.npz
7.  compute_eta_*.py        → eta_IB_*.npz + .txt
8.  compute_ricci*.py       → ricci_map_nside16.fits
9.  hyper_ib_cosmic.py      → hyper_ib_*.npz
10. tda_ripser.py            → phi_tda.npy
11. etf_correlation.py       → etf_*.npy, etf_results.txt
12. classify_cosmic_web.py   → classification_3d.npy
```

All pipeline scripts are included in `extracted/` and documented with inline comments.

---

## Troubleshooting

### `7z` not found

```bash
sudo apt install p7zip-full   # Ubuntu/Debian
brew install p7zip            # macOS
choco install 7zip            # Windows (Chocolatey)
winget install 7zip.7zip      # Windows (winget)
```

### Files extracted to wrong location

If files land directly in the repo root instead of `extracted/`:

```bash
mkdir -p extracted
mv *.fits *.npz *.npy *.png *.txt *.py extracted/ 2>/dev/null || true
```

### Fewer than 105 files after extraction

The archive download may be incomplete. Re-download and verify the SHA256 checksum (see top of this file).

### `healpy` import error on macOS arm64 / Apple Silicon

```bash
pip install healpy --no-binary healpy
# or:
conda install -c conda-forge healpy
```

### Custom data path

If your data lives outside the repository, use the `IB_DATA_DIR` environment variable:

```bash
export IB_DATA_DIR="/path/to/your/extracted"
streamlit run app.py
```

> **Do not commit binary data to Git.** All large files (`.fits`, `.npz`, `.npy`) are listed in `.gitignore`.
