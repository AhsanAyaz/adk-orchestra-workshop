#!/usr/bin/env bash
#
# ADK Orchestra Workshop — setup script
#
# Installs:
#   • Python virtual env + ADK dependencies
#   • Antigravity CLI (agy) — optional, prompted
#
# Re-run any time. Safe to run multiple times.
#
set -e

cd "$(dirname "$0")"

BOLD=$(tput bold 2>/dev/null || echo "")
DIM=$(tput dim 2>/dev/null || echo "")
GREEN=$(tput setaf 2 2>/dev/null || echo "")
YELLOW=$(tput setaf 3 2>/dev/null || echo "")
BLUE=$(tput setaf 4 2>/dev/null || echo "")
RESET=$(tput sgr0 2>/dev/null || echo "")

say()  { echo "${BLUE}▸${RESET} $*"; }
ok()   { echo "${GREEN}✓${RESET} $*"; }
warn() { echo "${YELLOW}!${RESET} $*"; }

# ── 1. Python version check ───────────────────────────────────────────────
say "Checking Python..."
if ! command -v python3 >/dev/null; then
    echo "${YELLOW}Python 3 not found. Install Python 3.10+ from python.org first.${RESET}"
    exit 1
fi
PY_VER=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
if ! python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)'; then
    echo "${YELLOW}Python ${PY_VER} found, but Python 3.10+ is required.${RESET}"
    exit 1
fi
ok "Python ${PY_VER} detected"

# ── 2. Virtual environment ────────────────────────────────────────────────
if [ ! -d .venv ]; then
    say "Creating virtual environment (.venv/)..."
    python3 -m venv .venv
    ok "venv created"
else
    ok "venv already exists"
fi

# ── 3. Python dependencies ────────────────────────────────────────────────
say "Installing Python dependencies..."
.venv/bin/pip install --upgrade pip -q
.venv/bin/pip install -r requirements.txt -q
ok "ADK + dependencies installed"

# ── 4. .env file ──────────────────────────────────────────────────────────
if [ ! -f .env ]; then
    cp .env.example .env
    warn "Created .env from .env.example — edit it and add your GOOGLE_API_KEY"
    warn "Get a free key at: https://aistudio.google.com/apikey"
else
    ok ".env already configured"
fi

# ── 5. Antigravity CLI ────────────────────────────────────────────────────
echo ""
say "Checking Antigravity CLI (optional, for vibe-coding bonus step)..."
if command -v agy >/dev/null 2>&1; then
    AGY_VER=$(agy --version 2>/dev/null || echo "installed")
    ok "Antigravity CLI already installed (${AGY_VER})"
else
    echo ""
    read -rp "Install Antigravity CLI (agy) now? [Y/n] " ans
    ans=${ans:-Y}
    if [[ "$ans" =~ ^[Yy]$ ]]; then
        say "Installing Antigravity CLI..."
        curl -fsSL https://antigravity.google/cli/install.sh | bash
        ok "Antigravity CLI installed — run 'agy' to start"
    else
        warn "Skipped. Install later with: curl -fsSL https://antigravity.google/cli/install.sh | bash"
    fi
fi

# ── Done ──────────────────────────────────────────────────────────────────
echo ""
echo "${BOLD}Setup complete.${RESET}"
echo ""
echo "Next steps:"
echo "  ${DIM}1.${RESET} Edit ${BOLD}.env${RESET} and add your GOOGLE_API_KEY"
echo "  ${DIM}2.${RESET} ${BOLD}source .venv/bin/activate${RESET}"
echo "  ${DIM}3.${RESET} ${BOLD}adk web${RESET}     ${DIM}# launches the agent playground${RESET}"
echo ""
echo "Workshop: open ${BOLD}index.html${RESET} in your browser."
