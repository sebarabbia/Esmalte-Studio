#!/usr/bin/env bash
# Publica el sitio: toma el diseño más reciente y le inyecta el <head> SEO.
# Uso:  ./build.sh ["Esmalte Studio v3.dc.html"]
set -e
cd "$(dirname "$0")"
SRC="${1:-Esmalte Studio v3.dc.html}"
python3 seo/build_index.py "$SRC"
echo "Listo. Revisá index.html y luego: git add -A && git commit && git push"
