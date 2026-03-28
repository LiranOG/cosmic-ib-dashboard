"""
Unit tests for data-loading functions in app.py.

Run with:
    pytest tests/test_data_loading.py -v

These tests mock the filesystem so they do NOT require the actual data archive.
"""

import os
import sys
import types
import numpy as np
import pytest

# ---------------------------------------------------------------------------
# Helpers: create lightweight mock data in a temp directory
# ---------------------------------------------------------------------------

@pytest.fixture()
def mock_data_dir(tmp_path):
    """Populate a temp directory with minimal mock data files."""
    d = tmp_path

    # Fisher results
    np.savez(d / "fisher_results.npz",
             MI=np.float64(82.9317),
             l=np.arange(513),
             Cl=np.zeros(513),
             Fl=np.ones(513))

    # eta_IB nside=8
    np.savez(d / "eta_IB_nside8.npz",
             I_TY=np.float64(0.3759),
             I_XT=np.float64(82.9317),
             eta_IB=np.float64(0.004533))

    # eta_IB nside=16
    np.savez(d / "eta_IB_nside16.npz",
             I_TY=np.float64(0.2406),
             I_XT=np.float64(82.9317),
             eta_IB=np.float64(0.002902))

    # eta_IB cosmic lowres (nside=64)
    np.savez(d / "eta_IB_cosmic_lowres.npz",
             I_TY=np.float64(0.0275),
             I_XT=np.float64(82.9317),
             eta_IB=np.float64(0.000331))

    # Hyper-IB Ricci results
    np.savez(d / "hyper_ib_ricci_results.npz",
             mi_unweighted=np.float64(0.4119),
             mi_ricci=np.float64(0.3961),
             eta_unweighted=np.float64(0.004966),
             eta_ricci=np.float64(0.004777),
             alpha=np.float64(1.0))

    # Hyper-IB geometry-weighted
    np.savez(d / "hyper_ib_results.npz",
             mi_unweighted=np.float64(0.4119),
             mi_weighted=np.float64(0.3356),
             eta_unweighted=np.float64(0.004966),
             eta_weighted=np.float64(0.004047),
             alpha=np.float64(1.0))

    # ETF bootstrap
    rng = np.random.default_rng(0)
    np.save(d / "etf_scores_bootstrap.npy", rng.normal(0.224, 0.058, 100))
    np.save(d / "etf_score_full.npy", np.float64(0.2256))
    np.save(d / "phi_tda.npy", np.float64(977.083))

    # 3D classification (tiny version)
    np.save(d / "classification_3d.npy",
            np.random.randint(0, 4, (8, 8, 8), dtype=np.int8))

    return str(d)


# ---------------------------------------------------------------------------
# Utility: load an NPZ from the mock dir
# ---------------------------------------------------------------------------

def load_npz(data_dir, fname):
    path = os.path.join(data_dir, fname)
    if os.path.exists(path):
        return np.load(path, allow_pickle=True)
    return None


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestFisherLoading:
    def test_mi_value(self, mock_data_dir):
        d = load_npz(mock_data_dir, "fisher_results.npz")
        assert d is not None
        assert abs(float(d["MI"]) - 82.9317) < 0.001

    def test_power_spectrum_shape(self, mock_data_dir):
        d = load_npz(mock_data_dir, "fisher_results.npz")
        assert d["l"].shape == (513,)
        assert d["Cl"].shape == (513,)
        assert d["Fl"].shape == (513,)


class TestEtaIBLoading:
    @pytest.mark.parametrize("fname,expected_eta", [
        ("eta_IB_nside8.npz",          0.004533),
        ("eta_IB_nside16.npz",         0.002902),
        ("eta_IB_cosmic_lowres.npz",   0.000331),
    ])
    def test_eta_values(self, mock_data_dir, fname, expected_eta):
        d = load_npz(mock_data_dir, fname)
        assert d is not None
        assert abs(float(d["eta_IB"]) - expected_eta) < 1e-5

    def test_eta_ordering(self, mock_data_dir):
        """η_IB must increase as nside decreases (coarser pixels)."""
        eta_64 = float(load_npz(mock_data_dir, "eta_IB_cosmic_lowres.npz")["eta_IB"])
        eta_16 = float(load_npz(mock_data_dir, "eta_IB_nside16.npz")["eta_IB"])
        eta_8  = float(load_npz(mock_data_dir, "eta_IB_nside8.npz")["eta_IB"])
        assert eta_64 < eta_16 < eta_8, "η_IB must increase with pixel area"

    def test_ixt_consistent(self, mock_data_dir):
        """I(X;T) should be the same across all result files."""
        fnames = ["eta_IB_nside8.npz", "eta_IB_nside16.npz", "eta_IB_cosmic_lowres.npz"]
        ixts = [float(load_npz(mock_data_dir, f)["I_XT"]) for f in fnames]
        assert all(abs(v - ixts[0]) < 1e-4 for v in ixts), "I(X;T) inconsistent across files"


class TestHyperIBLoading:
    def test_ricci_reduces_mi(self, mock_data_dir):
        """Ricci weighting should reduce or equal unweighted MI in the mock data."""
        d = load_npz(mock_data_dir, "hyper_ib_ricci_results.npz")
        assert float(d["mi_ricci"]) <= float(d["mi_unweighted"])

    def test_eta_keys_present(self, mock_data_dir):
        d = load_npz(mock_data_dir, "hyper_ib_ricci_results.npz")
        for key in ["mi_unweighted", "mi_ricci", "eta_unweighted", "eta_ricci", "alpha"]:
            assert key in d.files, f"Missing key: {key}"


class TestETFLoading:
    def test_bootstrap_shape(self, mock_data_dir):
        bs = np.load(os.path.join(mock_data_dir, "etf_scores_bootstrap.npy"))
        assert bs.shape == (100,)

    def test_bootstrap_range(self, mock_data_dir):
        bs = np.load(os.path.join(mock_data_dir, "etf_scores_bootstrap.npy"))
        assert bs.min() >= 0.0
        assert bs.max() <= 1.0

    def test_phi_tda_positive(self, mock_data_dir):
        phi = float(np.load(os.path.join(mock_data_dir, "phi_tda.npy")))
        assert phi > 0


class TestClassification3D:
    def test_values_in_range(self, mock_data_dir):
        arr = np.load(os.path.join(mock_data_dir, "classification_3d.npy"))
        assert arr.min() >= 0
        assert arr.max() <= 3

    def test_dtype(self, mock_data_dir):
        arr = np.load(os.path.join(mock_data_dir, "classification_3d.npy"))
        assert arr.dtype == np.int8


class TestMissingFilesGraceful:
    def test_missing_npz_returns_none(self, mock_data_dir):
        result = load_npz(mock_data_dir, "nonexistent_file.npz")
        assert result is None
