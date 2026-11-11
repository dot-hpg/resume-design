#!/usr/bin/env bash
# Cut the next version of one resume track.
#   ./scripts/new_version.sh data-analyst
#   ./scripts/new_version.sh ai-engineer
# Copies <track>/v<latest>/ to <track>/v<latest+1>/ and renames the _vN file
# suffixes. Old versions are never modified.
set -euo pipefail

track="${1:-}"
root="$(cd "$(dirname "$0")/.." && pwd)"
case "$track" in
  data-analyst|ai-engineer) ;;
  *) echo "usage: $0 data-analyst|ai-engineer" >&2; exit 1 ;;
esac

dir="$root/$track"
latest=$(find "$dir" -maxdepth 1 -type d -name 'v[0-9]*' -printf '%f\n' \
  | sed 's/^v//' | sort -n | tail -1)
[ -n "$latest" ] || { echo "no versions found in $dir" >&2; exit 1; }
next=$((latest + 1))
src="$dir/v$latest"; dst="$dir/v$next"
[ ! -e "$dst" ] || { echo "$dst already exists" >&2; exit 1; }

cp -r "$src" "$dst"
for f in "$dst"/*_v"$latest".*; do
  [ -e "$f" ] && mv "$f" "${f/_v$latest./_v$next.}"
done

echo "Created $track/v$next from v$latest. Next steps:"
echo "  1. Edit the files in $track/v$next/ and re-export the PDF"
echo "  2. pdftotext -layout $track/v$next/*.pdf $track/v$next/resume.txt"
echo "  3. Add a v$next entry to $track/CHANGELOG.md and update README.md"
echo "  4. git add $track README.md && git commit -m \"$track: v$next - <summary>\""
echo "  5. git tag $track-v$next && git push origin main --tags"
