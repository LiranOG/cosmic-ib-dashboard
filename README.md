# 🌌 Cosmic-Scale Information Bottleneck Efficiency Dashboard

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.32+-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![HEALPix](https://img.shields.io/badge/HEALPix-healpy-orange.svg)](https://healpy.readthedocs.io)
[![SDSS DR18](https://img.shields.io/badge/data-SDSS%20DR18-brightgreen.svg)](https://www.sdss4.org/dr18/)

> An interactive academic dashboard for exploring the cosmic-scale Information Bottleneck efficiency η_IB as a partial empirical test of the Universal Information Bottleneck Invariance Conjecture (UIBIC) from the Fractal Cosmopsychism Model (FCM).

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Data Requirements](#data-requirements)
- [Installation](#installation)
- [Data Setup](#data-setup)
- [Running the Dashboard](#running-the-dashboard)
- [Docker](#docker)
- [Deployment](#deployment)
- [Customisation](#customisation)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [References](#references)

---

## Overview

This dashboard implements a complete interactive analysis pipeline for the study:

> *"How efficiently does the large-scale galaxy density field T compress primordial information X (the CMB power spectrum) into galaxy cluster abundance Y?"*

The **Information Bottleneck efficiency** is defined as:

```
η_IB = I(T ; Y) / I(X ; T)
```

where:
| Symbol | Meaning |
|--------|---------|
| **X** | Primordial information field — approximated by the CMB angular power spectrum |
| **T** | Galaxy density field — HEALPix map built from SDSS DR18 spectroscopic galaxies |
| **Y** | Galaxy cluster abundance — redMaPPer DR8 cluster counts per HEALPix pixel |
| **R** | Ollivier–Ricci curvature of the cosmic web |
| **Φ_TDA** | Topological Data Analysis persistence measure |
| **ETF** | Entropy Transfer Function score |

The **UIBIC prediction** for the cosmic scale (n=5) is η_IB ≈ 0.42 ± 0.14. This study
measures η_IB ≈ 0.0045 using SDSS data, finding a ~93× gap that is attributed to scale mismatch
and survey depth limitations.

---

## Features

| Section | Visualisations |
|---------|---------------|
| 🏠 Introduction | Key metric cards, density sky map, variable definitions |
| 📊 Data Overview | **3D galaxy scatter** (Plotly), cosmic web **pie chart**, HEALPix resolution table |
| 🔬 Results & η_IB | Full **results table** (CSV download), 6 scatter plots, **interactive OLS scatter**, **2D joint heatmap P(T,Y)** |
| 📈 Scale Dependence | **Log-log line plot** η_IB vs nside with UIBIC band, **power-law fit**, estimator comparison bar chart, density/cluster histograms |
| 🌀 Hyper-IB & Ricci | **Bar chart** unweighted vs Ricci-weighted MI, **Ricci curvature Mollweide map** |
| 🔷 Topology & ETF | **Box plot** + **histogram** + normal overlay (bootstrap ETF), **T-Web decision tree** diagram |
| 🗺️ Sky Maps | Mollweide density + cluster maps, **interactive Fisher power spectrum** C_ℓ |
| 🔗 Networks | **Variable dependency graph** (NetworkX), **Venn diagram** (X, T, Y information overlap) |
| 📐 Pipeline | End-to-end **analysis flowchart**, **MI algorithm flowchart**, **analysis timeline** |
| 🖼️ Gallery | All PNG outputs from the archive |
| 📚 Conclusions | Summary infographic, references, full CSV download |

---

## Screenshots

> Place screenshots in a `docs/screenshots/` folder and reference them here once the app is running.

```
docs/
└── screenshots/
    ├── intro.png
    ├── results.png
    ├── scale_dependence.png
    └── network.png
```

---

## Data Requirements

The app reads pre-computed results from a folder named `extracted/` placed alongside `app.py`.
This folder is produced by extracting the companion archive `files.7z` (≈27 MB compressed,
≈136 MB uncompressed, 105 files).

### Required files (minimum viable set)

| File | Type | Source / Description |
|------|------|---------------------|
| `density_map.png` | PNG | Full-res SDSS galaxy density sky map |
| `cluster_map.png` | PNG | redMaPPer cluster count sky map |
| `power_spectrum.png` | PNG | Angular power spectrum C_ℓ of density field |
| `hyper_ib_ricci_results.png` | PNG | Ricci-weighted MI visualisation |
| `hyper_ib_scatter.png` | PNG | Curvature vs MI contribution scatter |
| `etf_correlation.png` | PNG | ETF feature–target correlation plot |
| `eta_IB_cosmic_scatter_lowres.png` | PNG | T vs Y scatter at nside=64 |
| `eta_IB_nside16_scatter.png` | PNG | T vs Y scatter at nside=16 |
| `eta_IB_nside8_scatter.png` | PNG | T vs Y scatter at nside=8 |
| `eta_IB_abundance_scatter.png` | PNG | Abundance estimator scatter |
| `eta_IB_wide_scatter.png` | PNG | Wide-z sample scatter |
| `eta_IB_count_scatter.png` | PNG | Raw count estimator scatter |
| `fisher_results.npz` | NumPy | Fisher MI (I(X;T)=82.93 nats), C_ℓ, F_ℓ arrays |
| `eta_IB_nside8.npz` | NumPy | I(T;Y), η_IB at nside=8 |
| `eta_IB_nside16.npz` | NumPy | I(T;Y), η_IB at nside=16 |
| `eta_IB_cosmic_lowres.npz` | NumPy | I(T;Y), η_IB at nside=64 |
| `hyper_ib_ricci_results.npz` | NumPy | Ricci-weighted MI results |
| `hyper_ib_results.npz` | NumPy | Geometry-weighted MI results |
| `etf_scores_bootstrap.npy` | NumPy | 100 bootstrap ETF scores |
| `etf_score_full.npy` | NumPy | Full-sample ETF score (scalar) |
| `phi_tda.npy` | NumPy | Φ_TDA persistence scalar |
| `classification_3d.npy` | NumPy | 128³ T-Web cosmic web classification |
| `density_nside16.fits` | HEALPix FITS | Galaxy density map at nside=16 |
| `cluster_count_nside16.fits` | HEALPix FITS | Cluster count map at nside=16 |
| `ricci_map_nside16.fits` | HEALPix FITS | Ollivier–Ricci curvature map at nside=16 |
| `large_sample.fits` | FITS | SDSS DR18 spectroscopic galaxy catalog (75,770 rows) |

### Optional / supplementary files

All remaining `.fits`, `.py`, `.txt`, `.npz`, and `.npy` files in the archive enhance
specific sections but the app will load gracefully without them.

### Obtaining the data

The pre-computed archive is the primary route. If you want to reproduce results from scratch:

1. **Galaxy catalog** — Query SDSS DR18 via [CasJobs](https://skyserver.sdss.org/casjobs/) using
   the SQL in `scripts/sdss_query.sql` (see `data/README.md`).
2. **Cluster catalog** — Download `cat_dr8.fits` from
   [VizieR J/ApJS/785/104](https://vizier.cds.unistra.fr/viz-bin/VizieR?-source=J/ApJS/785/104)
   (Rykoff et al. 2014).
3. **HEALPix maps** — Run the pipeline scripts in `extracted/` (e.g. `build_density_map.py`,
   `create_maps_nside16.py`, etc.).
4. **Fisher & MI results** — Execute `fisher_analysis.py`, `compute_eta_IB_cosmic.py`, etc.

---

## Installation

### Prerequisites

- Python **3.10+**
- `pip` or `conda`
- `p7zip` (to extract the `.7z` archive): `sudo apt install p7zip-full` / `brew install p7zip`
- Optional: `healpy` requires a C compiler and CFITSIO (usually available via pip on Linux/macOS)

### 1 — Clone the repository

```bash
git clone https://github.com/<your-username>/cosmic-ib-dashboard.git
cd cosmic-ib-dashboard
```

### 2 — Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

### 3 — Install Python dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **Tip:** If `healpy` fails to install on Windows, use WSL2 or the Docker route described below.

---

## Data Setup

### Extract the archive

Place `files.7z` in the repository root, then run:

```bash
bash scripts/extract_data.sh
```

Or manually:

```bash
7z x files.7z -oextracted/
```

The app expects an `extracted/` folder **in the same directory as `app.py`**:

```
cosmic-ib-dashboard/
├── app.py
├── extracted/          ← unpack files.7z here
│   ├── density_map.png
│   ├── density_nside16.fits
│   ├── fisher_results.npz
│   └── ...
└── ...
```

### Using a custom path

If your data lives elsewhere, edit the single line in `app.py`:

```python
# Line ~65 in app.py
DATA_DIR = os.path.join(os.path.dirname(__file__), "extracted")
# Change to, e.g.:
DATA_DIR = "/path/to/your/data"
```

---

##  Data Requirements

The dashboard requires pre‑computed data files that are **not included in this repository** due to size constraints.

### Quick Download

The easiest way to get the data:

```bash
bash scripts/download_data.sh
```

This script will:

Download files.7z from the GitHub Release

Extract it to the extracted/ folder

Remove the compressed archive

---

##  Manual Download

If the script doesn't work on your system:

Go to: https://github.com/LiranOG/cosmic-ib-dashboard/releases

Download the latest files.7z asset

Place it in the project root

Extract: 7z x files.7z -oextracted/

Note: The app expects the extracted files in a folder named extracted/ alongside app.py.

What's Inside

The archive contains 105 files (~136 MB uncompressed) including:

HEALPix sky maps (density, cluster counts, Ricci curvature)

Mutual information results at multiple resolutions (nside=8, 16, 32, 64)

Fisher analysis data (I(X;T)=82.93I(X;T)=82.93 nats)

Topological persistence data (ΦTDA=977Φ TDA​ =977)

ETF scores and bootstrap distributions

SDSS galaxy and redMaPPer cluster catalogs (FITS format)

All visualisations (PNG) used in the dashboard

For a complete file list, see data/README.md.

Verification
After extraction, verify that the extracted/ folder exists and contains files:

```
bash
ls extracted/ | head -10
You should see files like density_map.png, fisher_results.npz, etc.
```

You should see files like density_map.png, fisher_results.npz, etc.


---

## Running the Dashboard

### Local (recommended for development)

```bash
streamlit run app.py
```

The dashboard opens automatically at **http://localhost:8501**.

### Quick Start

```bash
# Clone → extract data → install → run (all in one block)
git clone https://github.com/<your-username>/cosmic-ib-dashboard.git
cd cosmic-ib-dashboard
bash scripts/extract_data.sh          # requires files.7z in repo root
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

### Available command-line options

```bash
streamlit run app.py \
  --server.port 8502 \
  --server.headless true \
  --theme.base dark
```

---

## Docker

### Build the image

```bash
docker build -t cosmic-ib-dashboard .
```

### Run (mounting extracted data)

```bash
docker run -p 8501:8501 \
  -v "$(pwd)/extracted:/app/extracted" \
  cosmic-ib-dashboard
```

Open **http://localhost:8501** in your browser.

### Build with data baked in

```bash
# Copy data first, then build
cp -r extracted/ docker-data/
docker build -t cosmic-ib-dashboard-with-data \
  --build-arg DATA_DIR=docker-data .
```

---

## Deployment

### Streamlit Community Cloud (free tier)

1. Push the repository to GitHub (ensure `extracted/` is **not** committed — it is in `.gitignore`).
2. Host your data on a cloud storage bucket (S3, GCS) or use Git LFS for small files.
3. Add a startup script in `.streamlit/secrets.toml` to download the data at boot, or modify
   `app.py` to fetch from a URL.
4. Connect the repo at [share.streamlit.io](https://share.streamlit.io) and set
   `app.py` as the main file.

### Heroku

```bash
heroku create cosmic-ib-dashboard
heroku buildpacks:add heroku/python
git push heroku main
```

Add a `Procfile`:

```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

### Google Cloud Run / AWS App Runner

Use the provided `Dockerfile` and follow the respective platform's container deployment guide.
Data should be mounted from Cloud Storage or baked into the image.

---

## Customisation

### Changing the colour theme

Edit `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#06d6a0"    # change accent colour
backgroundColor = "#0b0e1a"
```

Or modify the CSS variables at the top of `app.py` (`--accent`, `--accent2`, etc.).

### Adding a new nside resolution

1. Compute maps and MI with your preferred scripts.
2. Save results as `extracted/eta_IB_nsideN.npz` with keys `I_TY`, `I_XT`, `eta_IB`.
3. In `load_all_data()` inside `app.py`, add an analogous block:
   ```python
   d = load_npz_safe("eta_IB_nside4.npz")
   results.append(dict(nside=4, I_TY=float(d["I_TY"]), ...))
   ```

### Swapping the galaxy catalog

Replace `large_sample.fits` with any FITS file that contains `ra`, `dec`, `z` columns
and update the column names in the Data Overview section of `app.py` (~line 135).

### Disabling sections

Comment out the corresponding `elif` block in `app.py` and remove the entry from the
sidebar `st.radio` list.

---

## Contributing

We welcome all contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for full details.

**Quick guide:**

1. Fork the repository and create a feature branch: `git checkout -b feature/my-feature`
2. Make changes, add tests if applicable, and commit: `git commit -m "feat: add my feature"`
3. Push to your fork: `git push origin feature/my-feature`
4. Open a Pull Request with a clear description of the changes.

---

## License

This project is released under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## Acknowledgments

- **SDSS** — Funding for SDSS-IV has been provided by the Alfred P. Sloan Foundation, the U.S.
  Department of Energy Office of Science, and the Participating Institutions. SDSS acknowledges
  support and resources from the Center for High-Performance Computing at the University of Utah.
- **redMaPPer** — E. S. Rykoff et al. (2014), cluster catalog originally derived from SDSS DR8
  photometry.
- **HEALPix / healpy** — K. M. Górski et al. (2005), NASA / JPL-Caltech.
- **Streamlit** — The Streamlit open-source team.
- **Plotly** — Plotly Technologies Inc.

---

## Data Sources
|Dataset | Source | Reference|
|------------|---------------|
| SDSS DR18 | SDSS | CasJobs | https://www.sdss.org/dr18 |
| redMaPPer | DR8 | VizieR | (J/ApJS/785/104) | Rykoff et al. 2014 |
| HEALPix | Maps | Custom processing | Górski et al. 2005 |
| Fisher Analysis | Custom processing | This work |

## References

| Citation | Description |
|----------|-------------|
| Tishby, Pereira & Bialek (2000) | *The Information Bottleneck Method* — NeurIPS 2000 |
| Rykoff et al. (2014) | *redMaPPer I: Algorithm and SDSS DR8 Catalog* — ApJS 224, 1 |
| Górski et al. (2005) | *HEALPix: A Framework for High-Resolution Discretization* — ApJ 622, 759 |
| Ollivier (2009) | *Ricci curvature of Markov chains on metric spaces* — J. Funct. Anal. 256, 810 |
| Hahn et al. (2007) | *Properties of dark matter halos in clusters, filaments, sheets and voids* — MNRAS 375, 489 |
| Edelsbrunner & Harer (2008) | *Persistent Homology — A Survey* — AMS Contemporary Mathematics |
| Weygaert & Bond (2008) | *Clusters and the Theory of the Cosmic Web* — LNP 740 |
| SDSS DR18 (2023) | *The Seventeenth Data Release of the SDSS* — ApJS 267, 44 |
