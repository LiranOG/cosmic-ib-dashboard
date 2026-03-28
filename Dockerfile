# ── Stage: builder ────────────────────────────────────────────────────────────
# Install system deps and Python packages in a separate layer so the final
# image doesn't carry build tools.
FROM python:3.10-slim AS builder

WORKDIR /build

# System dependencies required by healpy / astropy / matplotlib
RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc \
        g++ \
        libcfitsio-dev \
        pkg-config \
        libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install into a prefix so we can copy cleanly
RUN pip install --upgrade pip \
 && pip install --prefix=/install --no-cache-dir -r requirements.txt


# ── Stage: runtime ────────────────────────────────────────────────────────────
FROM python:3.10-slim

LABEL maintainer="your-email@example.com"
LABEL description="Cosmic-Scale Information Bottleneck Efficiency — Streamlit Dashboard"
LABEL version="1.0.0"

WORKDIR /app

# Minimal runtime system libs (healpy needs cfitsio at runtime)
RUN apt-get update && apt-get install -y --no-install-recommends \
        libcfitsio10 \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application source
COPY app.py .
COPY .streamlit/ .streamlit/

# The extracted/ data folder should be mounted at runtime:
#   docker run -v $(pwd)/extracted:/app/extracted ...
# Alternatively, uncomment the next line to bake data into the image:
# COPY extracted/ extracted/

# Create a non-root user for security
RUN useradd -m -u 1000 appuser \
 && chown -R appuser:appuser /app
USER appuser

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/_stcore/health')"

ENTRYPOINT ["streamlit", "run", "app.py", \
            "--server.port=8501", \
            "--server.address=0.0.0.0", \
            "--server.headless=true", \
            "--browser.gatherUsageStats=false"]
