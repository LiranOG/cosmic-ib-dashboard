# 🌌 Cosmic-Scale Information Bottleneck Efficiency Dashboard

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit 1.32+](https://img.shields.io/badge/streamlit-1.32%2B-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![HEALPix](https://img.shields.io/badge/HEALPix-healpy-orange.svg)](https://healpy.readthedocs.io)
[![SDSS DR18](https://img.shields.io/badge/data-SDSS%20DR18-brightgreen.svg)](https://www.sdss4.org/dr18/)

> An interactive academic dashboard for exploring the cosmic-scale Information Bottleneck
> efficiency **η_IB** as a partial empirical test of the Universal Information Bottleneck
> Invariance Conjecture (UIBIC) from the Fractal Cosmopsychism Model (FCM).

---

## 📋 Table of Contents

- [Overview](#overview)
- [Live Demo](#live-demo)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Quick Start](#quick-start)
- [Data Requirements](#data-requirements)
- [Installation](#installation)
- [Data Setup](#data-setup)
- [Running the Dashboard](#running-the-dashboard)
- [Running Tests](#running-tests)
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

> *"How efficiently does the large-scale galaxy density field **T** compress primordial information
> **X** (the CMB power spectrum) into galaxy cluster abundance **Y**?"*

The **Information Bottleneck efficiency** is defined as:

```
η_IB = I(T ; Y) / I(X ; T)
```

| Symbol | Meaning |
|--------|---------|
| **X** | Primordial information field — CMB angular power spectrum |
| **T** | Galaxy density field — HEALPix map (SDSS DR18 spectroscopic galaxies) |
| **Y** | Galaxy cluster abundance — redMaPPer DR8 cluster counts per pixel |
| **R** | Ollivier–Ricci curvature of the cosmic web |
| **Φ_TDA** | Topological Data Analysis persistence measure |
| **ETF** | Entropy Transfer Function score |

The **UIBIC prediction** for the cosmic scale (n=5) is **η_IB ≈ 0.42 ± 0.14**.  
This study measures **η_IB ≈ 0.0045**, finding a ~93× gap attributed to scale mismatch
and survey depth limitations.

---

## Live Demo

> 🚧 **Streamlit Cloud deployment coming soon.**  
> In the meantime, follow the [Quick Start](#quick-start) instructions to run locally.

---

## Features

| Section | Visualisations |
|---------|----------------|
| 🏠 Introduction | Key metric cards, density sky map, variable definitions |
| 📊 Data Overview | **3D galaxy scatter** (Plotly), cosmic web **pie chart**, HEALPix resolution table |
| 🔬 Results & η_IB | Full **results table** + CSV download, 6 scatter plots, **interactive OLS scatter**, **2D joint heatmap** P(T,Y) |
| 📈 Scale Dependence | **Log-log line plot** η_IB vs nside + UIBIC band, **power-law fit**, estimator comparison, density/cluster histograms |
| 🌀 Hyper-IB & Ricci | **Bar chart** unweighted vs Ricci-weighted MI, **Ricci curvature Mollweide map** |
| 🔷 Topology & ETF | **Box plot** + **histogram** + normal overlay (bootstrap ETF), **T-Web decision tree** diagram |
| 🗺️ Sky Maps | Mollweide density + cluster maps, **interactive Fisher power spectrum** C_ℓ |
| 🔗 Networks | **Variable dependency graph** (NetworkX), **Venn diagram** (X, T, Y information overlap) |
| 📐 Pipeline | End-to-end **analysis flowchart**, **MI algorithm flowchart**, **analysis timeline** (Gantt) |
| 🖼️ Gallery | All PNG outputs from the archive |
| 📚 Conclusions | Summary infographic, references, full CSV download |

---

## Repository Structure

```
cosmic-ib-dashboard/
├── app.py                          # Main Streamlit dashboard (~600 lines)
├── requirements.txt                # Pinned Python dependencies
├── environment.yml                 # Conda environment spec
├── pytest.ini                      # pytest configuration
├── Dockerfile                      # Multi-stage Docker build
├── CONTRIBUTING.md                 # Contribution guidelines
├── LICENSE                         # MIT License
├── README.md                       # This file
│
├── .github/
│   ├── workflows/
│   │   └── ci.yml                  # GitHub Actions CI (test + lint)
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
│
├── .streamlit/
│   └── config.toml                 # Dark theme configuration
│
├── data/
│   └── README.md                   # Complete data file inventory (105 files)
│
├── docs/
│   ├── architecture.md             # Data flow & module explanations
│   └── screenshots/                # UI screenshots (add after first run)
│
├── scripts/
│   ├── download_data.sh            # Auto-download data from GitHub Releases (Linux/macOS)
│   ├── download_data.bat           # Windows equivalent
│   └── extract_data.sh             # Extraction helper (idempotent)
│
├── notebooks/
│   └── exploration.ipynb           # Interactive data exploration notebook
│
└── tests/
    └── test_data_loading.py        # 15+ unit tests (all mock-based, no data required)
```

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/LiranOG/cosmic-ib-dashboard.git
cd cosmic-ib-dashboard

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Download and extract data (~136 MB uncompressed, 105 files)
bash scripts/download_data.sh      # Downloads from GitHub Releases automatically

# 5. Launch the dashboard
streamlit run app.py
# → Opens at http://localhost:8501
```

---

## Data Requirements

The app reads pre-computed results from a folder named `extracted/` placed alongside `app.py`.
This folder is produced by extracting the companion archive `files.7z`
(≈27 MB compressed, ≈136 MB uncompressed, 105 files).

### Obtaining the data

**Option A — Automated (recommended):**

```bash
bash scripts/download_data.sh
```

This script will:
1. Detect whether `curl` or `wget` is available
2. Fetch the latest `files.7z` from the GitHub Releases page
3. Extract it to `extracted/`
4. Verify the file count

**Option B — Manual:**

1. Go to [Releases](https://github.com/LiranOG/cosmic-ib-dashboard/releases)
2. Download `files.7z` from the latest release
3. Place it in the repository root
4. Run:
   ```bash
   bash scripts/extract_data.sh
   # or directly:
   7z x files.7z -oextracted/
   ```

**Option C — Windows (PowerShell / batch):**

```bat
scripts\download_data.bat
```

### Verifying the extraction

```bash
ls extracted/ | wc -l   # should print 105
```

For a complete listing of all 105 files, see [`data/README.md`](data/README.md).

### Custom data path

If your data lives outside the repository, set the `IB_DATA_DIR` environment variable:

```bash
export IB_DATA_DIR="/path/to/your/extracted"
streamlit run app.py
```

---

## Installation

### Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| Python | 3.10+ | [python.org](https://python.org) |
| pip | latest | bundled with Python |
| p7zip | any | `sudo apt install p7zip-full` / `brew install p7zip` |
| Git | any | [git-scm.com](https://git-scm.com) |

> **Windows users:** `healpy` requires a C compiler. Use [WSL2](https://docs.microsoft.com/en-us/windows/wsl/) or the [Docker](#docker) route.

### Step-by-step

```bash
# Clone
git clone https://github.com/LiranOG/cosmic-ib-dashboard.git
cd cosmic-ib-dashboard

# Virtualenv
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# Upgrade pip and install
pip install --upgrade pip
pip install -r requirements.txt
```

### Conda (alternative)

```bash
conda env create -f environment.yml
conda activate cosmic-ib
```

---

## Data Setup

```bash
# Place files.7z in the repo root, then:
bash scripts/extract_data.sh

# Expected output:
# ✅ Extraction complete.
#    Files in extracted/: 105
```

The app expects:

```
cosmic-ib-dashboard/
├── app.py
└── extracted/          ← unpack files.7z here
    ├── density_map.png
    ├── density_nside16.fits
    ├── fisher_results.npz
    └── ...  (102 more files)
```

---

## Running the Dashboard

```bash
streamlit run app.py
```

The dashboard opens automatically at **http://localhost:8501**.

### Optional flags

```bash
streamlit run app.py \
  --server.port 8502 \
  --server.headless true \
  --theme.base dark
```

---

## Running Tests

Tests are fully mocked — **no data files required**.

```bash
# Run all tests
pytest

# Verbose output
pytest -v

# With coverage
pip install pytest-cov
pytest --cov=app --cov-report=html
```

Expected output:

```
tests/test_data_loading.py ................... [100%]
21 passed in 0.45s
```

Test categories:

| Class | What is tested |
|-------|---------------|
| `TestFisherLoading` | Fisher MI value, power spectrum array shapes |
| `TestEtaIBLoading` | η_IB values per nside, monotonic ordering, I(X;T) consistency |
| `TestHyperIBLoading` | Ricci weighting effect, required NPZ keys |
| `TestETFLoading` | Bootstrap array shape/range, Φ_TDA positivity |
| `TestClassification3D` | Value range [0,3], dtype int8 |
| `TestMissingFilesGraceful` | Graceful None return for missing files |
| `TestComputedQuantities` | η_IB formula consistency, pixel area formula |

---

## Docker

### Build

```bash
docker build -t cosmic-ib-dashboard .
```

### Run (mounting pre-extracted data)

```bash
docker run -p 8501:8501 \
  -v "$(pwd)/extracted:/app/extracted" \
  cosmic-ib-dashboard
```

Open **http://localhost:8501**.

### Build with data baked in

```bash
# Extract data first, then build
docker build -t cosmic-ib-dashboard-data .
# uncomment the COPY line in Dockerfile before building
```

---

## Deployment

### Streamlit Community Cloud

1. Push the repo to GitHub (`extracted/` is excluded by `.gitignore`).
2. Host `files.7z` on a cloud bucket or GitHub Releases.
3. Add a startup download script or fetch from URL in `app.py`.
4. Connect at [share.streamlit.io](https://share.streamlit.io) with `app.py` as entry point.

### Heroku

```bash
heroku create cosmic-ib-dashboard
heroku buildpacks:add heroku/python
git push heroku main
```

`Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

### Google Cloud Run / AWS App Runner

Use the provided `Dockerfile`. Mount data from Cloud Storage or bake into the image.

---

## Customisation

### Colour theme

Edit `.streamlit/config.toml` or the CSS variables at the top of `app.py`:

```toml
[theme]
primaryColor    = "#06d6a0"   # change accent colour
backgroundColor = "#0b0e1a"
```

### Adding a new HEALPix resolution

1. Compute maps and MI results, save as `extracted/eta_IB_nsideN.npz` with keys `I_TY`, `I_XT`, `eta_IB`.
2. In `load_all_data()` inside `app.py`, add:
   ```python
   d = load_npz_safe("eta_IB_nside4.npz")
   if d is not None:
       results.append(dict(nside=4, I_TY=float(d["I_TY"]), ...))
   ```

### Swapping the galaxy catalog

Replace `large_sample.fits` with any FITS file containing `ra`, `dec`, `z` columns and update
the column names in the **Data Overview** section (~line 135 of `app.py`).

---

## Contributing

We welcome all contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

**Quick guide:**
```bash
git checkout -b feature/my-feature
# make changes
black app.py && ruff check app.py --fix
pytest
git commit -m "feat: add my feature"
git push origin feature/my-feature
# open a Pull Request
```

---

## License

Released under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## Acknowledgments

- **SDSS** — Funding for SDSS-IV has been provided by the Alfred P. Sloan Foundation, the
  U.S. Department of Energy Office of Science, and the Participating Institutions.
- **redMaPPer** — E. S. Rykoff et al. (2014), derived from SDSS DR8 photometry.
- **HEALPix / healpy** — K. M. Górski et al. (2005), NASA / JPL-Caltech.
- **Streamlit** — The Streamlit open-source team.
- **Plotly** — Plotly Technologies Inc.
- **scikit-learn** — The scikit-learn contributors.

---

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
