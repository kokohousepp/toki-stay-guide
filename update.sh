#!/usr/bin/env bash
# 動画リンクを差し替えるヘルパー。
# 使い方: ./update.sh <スラッグ> <YouTubeのURL>
#   例:   ./update.sh washer https://youtu.be/abcd1234
# 有効なスラッグは links.json のキー（access, aircon, gomi, fridge, microwave,
#   washer, ricecooker, bath, 403-entry, 405-entry）。
set -e
cd "$(dirname "$0")"
SLUG="$1"
URL="$2"
if [ -z "$SLUG" ] || [ -z "$URL" ]; then
  echo "使い方: ./update.sh <スラッグ> <YouTubeのURL>"
  echo "有効なスラッグ: $(python3 -c 'import json;print(", ".join(json.load(open("links.json"))))')"
  exit 1
fi
python3 - "$SLUG" "$URL" <<'PY'
import json, sys
slug, url = sys.argv[1], sys.argv[2]
d = json.load(open("links.json", encoding="utf-8"))
if slug not in d:
    print("不明なスラッグ:", slug)
    print("有効:", ", ".join(d))
    sys.exit(1)
d[slug] = url
json.dump(d, open("links.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("更新:", slug, "->", url)
PY
python3 build.py
git add -A
git commit -m "update link: $SLUG"
git push
echo "完了。反映まで数十秒〜1分ほどです。"
