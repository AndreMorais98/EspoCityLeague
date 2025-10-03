# syntax=docker/dockerfile:1

# Use latest LTS of Python (Debian Bookworm-based). Adjust version if you need a specific LTS.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/.local/bin:${PATH}"

# Install system dependencies commonly useful for Python dev (build tools, git, curl)
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
       build-essential \
       curl \
       git \
       pkg-config \
       ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Use Poetry with pyproject.toml for dependency management
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir poetry

# Copy dependency manifests first to leverage Docker layer caching
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-interaction --no-ansi --no-root

# Copy the rest of the application source
COPY . .

# Default command: open a shell for interactive development
CMD ["bash"]


