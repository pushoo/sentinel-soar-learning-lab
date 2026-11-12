#!/usr/bin/env bash
# Learning lab: checks the tools this repo uses. Read-only; installs nothing.
set -uo pipefail

ok()   { printf "  [ok]      %s\n" "$1"; }
miss() { printf "  [missing] %s  ->  %s\n" "$1" "$2"; }

have() { command -v "$1" >/dev/null 2>&1; }

echo "Sentinel + SOAR learning lab: prerequisite check"
echo

echo "Machine"
os="$(uname -s)"; arch="$(uname -m)"
if [ "$os" = "Darwin" ]; then
  mem_gb=$(( $(sysctl -n hw.memsize) / 1024 / 1024 / 1024 ))
else
  mem_gb=$(( $(awk '/MemTotal/ {print $2}' /proc/meminfo) / 1024 / 1024 ))
fi
echo "  OS: $os  Arch: $arch  RAM: ${mem_gb} GB"
if [ "$mem_gb" -lt 12 ]; then
  echo "  Note: under 12 GB RAM. Run Shuffle + TheHive on a separate VM, or only one of them locally."
fi
echo

echo "Required"
if have python3; then ok "python3 $(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')"; else miss python3 "https://www.python.org/downloads/"; fi
if have git; then ok "git $(git --version | awk '{print $3}')"; else miss git "https://git-scm.com/downloads"; fi
if have az; then ok "azure-cli $(az version --query '"azure-cli"' -o tsv 2>/dev/null)"; else miss "azure-cli" "brew install azure-cli  (or Microsoft's installer)"; fi
echo

echo "Docker host (only needed where Shuffle/TheHive run)"
if have docker; then
  if docker info >/dev/null 2>&1; then
    ok "docker engine running ($(docker info --format '{{.OperatingSystem}}, {{.MemTotal}} bytes' 2>/dev/null))"
  else
    miss "docker engine" "docker CLI found but no engine running (start Colima or Docker Desktop)"
  fi
  if docker compose version >/dev/null 2>&1; then ok "docker compose $(docker compose version --short 2>/dev/null)"; else miss "docker compose" "install the compose plugin"; fi
else
  miss docker "Mac: brew install colima docker docker-compose | Ubuntu: soar/install-docker-ubuntu.sh"
fi
if [ "$os" = "Darwin" ]; then
  if have colima; then ok "colima $(colima version 2>/dev/null | head -1 | awk '{print $3}')"; else echo "  [optional] colima not installed (free, lightweight Docker VM for macOS)"; fi
fi
echo

echo "Optional"
if have curl; then ok "curl"; else miss curl "needed for the API examples"; fi
if have jq; then ok "jq"; else echo "  [optional] jq not installed (nicer JSON output)"; fi
echo
echo "Done. Nothing was changed on this machine."
