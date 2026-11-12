#!/usr/bin/env bash
# Learning lab: install Docker Engine + Compose plugin on Ubuntu (x86_64 or arm64) from Docker's apt repo.
set -euo pipefail

if [ "$(uname -s)" != "Linux" ] || ! grep -qi ubuntu /etc/os-release; then
  echo "This script is for Ubuntu. On macOS use Colima or Docker Desktop (see docs/00-prerequisites.md)." >&2
  exit 1
fi

sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# shellcheck disable=SC1091
. /etc/os-release
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu ${VERSION_CODENAME} stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list >/dev/null

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker "$USER"

# OpenSearch / Elasticsearch need this kernel setting.
echo "vm.max_map_count=262144" | sudo tee /etc/sysctl.d/99-soc-lab.conf >/dev/null
sudo sysctl --system >/dev/null

echo "Docker installed. Log out and back in (for the docker group), then run: docker run --rm hello-world"
