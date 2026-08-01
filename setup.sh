#!/usr/bin/env bash
# =============================================================================
# setup.sh — Operation Black Vault CTF — One-shot Organizer Setup Script
# =============================================================================
# Usage:
#   chmod +x setup.sh
#   ./setup.sh            # Full setup (Docker + Python deps + verify)
#   ./setup.sh --no-docker  # Skip Docker (Python deps only)
# =============================================================================

set -euo pipefail

# ── Colors ───────────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

SKIP_DOCKER=false

# ── Argument parsing ──────────────────────────────────────────────────────────
for arg in "$@"; do
  case $arg in
    --no-docker) SKIP_DOCKER=true ;;
    *) echo -e "${RED}Unknown argument: $arg${NC}"; exit 1 ;;
  esac
done

# ── Banner ────────────────────────────────────────────────────────────────────
echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║        OPERATION BLACK VAULT — CTF Setup Script             ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# ── Helper functions ──────────────────────────────────────────────────────────
info()    { echo -e "${CYAN}[INFO]${NC}  $1"; }
success() { echo -e "${GREEN}[OK]${NC}    $1"; }
warn()    { echo -e "${YELLOW}[WARN]${NC}  $1"; }
error()   { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }

# ── 1. Check Python ───────────────────────────────────────────────────────────
info "Checking Python version..."
if ! command -v python3 &>/dev/null; then
  error "Python 3 is not installed. Please install Python 3.10+."
fi
PY_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
success "Python $PY_VERSION found."

# ── 2. Install Python dependencies ───────────────────────────────────────────
info "Installing Python dependencies from requirements.txt..."
if [ -f "requirements.txt" ]; then
  python3 -m pip install --upgrade pip -q
  python3 -m pip install -r requirements.txt -q
  success "Python dependencies installed."
else
  warn "requirements.txt not found. Skipping Python deps."
fi

# ── 3. Check Docker ───────────────────────────────────────────────────────────
if [ "$SKIP_DOCKER" = false ]; then
  info "Checking Docker installation..."
  if ! command -v docker &>/dev/null; then
    error "Docker is not installed. Install Docker: https://docs.docker.com/get-docker/"
  fi
  success "Docker $(docker --version | awk '{print $3}' | tr -d ',') found."

  info "Checking Docker Compose..."
  if ! command -v docker-compose &>/dev/null && ! docker compose version &>/dev/null 2>&1; then
    error "Docker Compose not found. Install it: https://docs.docker.com/compose/install/"
  fi
  success "Docker Compose found."

  # ── 4. Build and launch web challenges ──────────────────────────────────────
  info "Building and launching web exploitation challenge containers..."
  if [ -f "docker-compose.yml" ]; then
    docker compose up -d --build
    success "All web challenge containers are running."
  else
    warn "Root docker-compose.yml not found. Trying web_exploitation/..."
    if [ -f "web_exploitation/docker-compose.yml" ]; then
      docker compose -f web_exploitation/docker-compose.yml up -d --build
      success "Web challenges launched from web_exploitation/."
    else
      warn "No docker-compose.yml found. Skipping container launch."
    fi
  fi
else
  info "Skipping Docker setup (--no-docker flag set)."
fi

# ── 5. Verify challenge files ─────────────────────────────────────────────────
info "Verifying challenge directory structure..."
CATEGORIES=("binary_exploitation" "cryptography" "digital_forensics" "miscellaneous" "reverse_engineering" "web_exploitation")
ALL_OK=true

for cat in "${CATEGORIES[@]}"; do
  if [ -d "$cat" ]; then
    success "  ✔ $cat/"
  else
    warn "  ✘ $cat/ — directory missing!"
    ALL_OK=false
  fi
done

if [ "$ALL_OK" = true ]; then
  success "All category directories present."
fi

# ── 6. Summary ────────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}${GREEN}════════════════════════════════════════${NC}"
echo -e "${BOLD}${GREEN}  OBV CTF Setup Complete!               ${NC}"
echo -e "${BOLD}${GREEN}════════════════════════════════════════${NC}"
echo ""
echo -e "  ${CYAN}Web Challenges:${NC}"
echo "    http://localhost:8001  — Ghost Signal (IDOR)"
echo "    http://localhost:8002  — Dead Drop (SQLi)"
echo "    http://localhost:8003  — Cipher Nest (JWT)"
echo "    http://localhost:8004  — Shadow Grid (SSTI)"
echo "    http://localhost:8005  — Blackout Protocol (SSRF)"
echo "    http://localhost:8006  — Vault Zero (Race Condition)"
echo ""
echo -e "  ${CYAN}Flag Format:${NC} BVAULT{...}"
echo -e "  ${CYAN}Docs:${NC}       See README.md and each category's ORGANIZER_MANUAL.md"
echo ""
