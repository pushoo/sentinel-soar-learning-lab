#!/usr/bin/env bash
# Learning lab: start TheHive 5 (minimal lab profile) with Docker Compose.
# For anything beyond a lab, use StrangeBee's official Docker profiles instead.
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
cd "$here/thehive"

if [ ! -f .env ]; then
  secret="$(LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c 40)"
  printf 'THEHIVE_SECRET=%s\n' "$secret" > .env
  chmod 600 .env
  echo "Generated soar/thehive/.env with a random application secret (git-ignored)."
fi

if [ "$(uname -s)" = "Linux" ]; then
  sudo sysctl -w vm.max_map_count=262144 >/dev/null
fi

docker compose up -d
docker compose ps
echo
echo "TheHive is starting (Cassandra and Elasticsearch first; give it 2-3 minutes)."
echo "Open http://<this-host>:9000  -  default login admin@thehive.local / secret  -  change it immediately."
echo "Then request a free Community license on the StrangeBee License Portal, or the UI stays read-only."
