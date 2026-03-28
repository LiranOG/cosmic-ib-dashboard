#!/usr/bin/env bash
# =============================================================================
# extract_data.sh
# Extracts files.7z into the extracted/ folder expected by app.py.
# Usage:  bash scripts/extract_data.sh [path/to/files.7z]
# =============================================================================

set -euo pipefail

ARCHIVE="${1:-files.7z}"
DEST_DIR="extracted"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "=== Cosmic-IB Dashboard — Data Extraction ==="
echo "Repository root : $REPO_ROOT"
echo "Archive         : $ARCHIVE"
echo "Destination     : $REPO_ROOT/$DEST_DIR/"
echo ""

# ── Check for p7zip ───────────────────────────────────────────────────────────
if ! command -v 7z &>/dev/null; then
    echo "ERROR: '7z' not found. Install p7zip:"
    echo "  Ubuntu/Debian : sudo apt install p7zip-full"
    echo "  macOS (brew)  : brew install p7zip"
    echo "  Windows       : choco install 7zip  OR  winget install 7zip.7zip"
    exit 1
fi

# ── Resolve archive path ──────────────────────────────────────────────────────
if [[ ! -f "$ARCHIVE" ]]; then
    # Try looking in repo root
    if [[ -f "$REPO_ROOT/$ARCHIVE" ]]; then
        ARCHIVE="$REPO_ROOT/$ARCHIVE"
    else
        echo "ERROR: Archive not found at '$ARCHIVE'."
        echo "Place files.7z in the repository root and re-run:"
        echo "  bash scripts/extract_data.sh"
        exit 1
    fi
fi

# ── Extract ───────────────────────────────────────────────────────────────────
mkdir -p "$REPO_ROOT/$DEST_DIR"

echo "Extracting '$ARCHIVE' → '$REPO_ROOT/$DEST_DIR/' ..."
7z x "$ARCHIVE" -o"$REPO_ROOT/$DEST_DIR/" -y

echo ""
echo "✅ Extraction complete."
echo "   Files in $DEST_DIR/: $(ls "$REPO_ROOT/$DEST_DIR/" | wc -l)"
echo ""
echo "Next step:"
echo "  source .venv/bin/activate && streamlit run app.py"
