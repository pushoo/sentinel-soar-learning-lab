#!/usr/bin/env bash
# Learning lab: install Shuffle (open-source SOAR) from its upstream repo, with lab memory caps.
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
vendor="$here/vendor"
mkdir -p "$vendor"

if [ ! -d "$vendor/Shuffle" ]; then
  git clone --depth 1 https://github.com/Shuffle/Shuffle "$vendor/Shuffle"
fi
cd "$vendor/Shuffle"

mkdir -p shuffle-database
if [ "$(uname -s)" = "Linux" ]; then
  sudo chown -R 1000:1000 shuffle-database
  sudo sysctl -w vm.max_map_count=262144 >/dev/null
fi

# Apply the memory caps only if the upstream compose file still has an "opensearch" service.
if docker compose config --services | grep -qx opensearch; then
  cp "$here/shuffle/docker-compose.override.yml" ./docker-compose.override.yml
  echo "Applied lab memory caps (docker-compose.override.yml)."
else
  echo "Upstream compose has no 'opensearch' service; skipping memory caps. Services found:" >&2
  docker compose config --services >&2
fi

docker compose up -d
docker compose ps
echo
echo "Shuffle is starting. Open https://<this-host>:3443 (or http://<this-host>:3001) and create the admin account."
echo "First start can take a few minutes while OpenSearch initialises."
