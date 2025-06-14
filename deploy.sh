#!/bin/bash
# deploy.sh for GitHub Pages in /docs

set -euo pipefail
cd "$(dirname "$0")"

python3 docs/gallery_generator.py

git add docs/
git commit -m "Automated update: gallery regen $(date +'%Y-%m-%d %H:%M')"
git push github gh-pages:main

