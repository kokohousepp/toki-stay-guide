#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# links.json を読んで、各スラッグの転送用 index.html を生成する。
# 使い方: python3 build.py
import json
import os
import html

ROOT = os.path.dirname(os.path.abspath(__file__))

TEMPLATE = """<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>TOKI STAY 動画ガイド</title>
<meta http-equiv="refresh" content="0; url={url_attr}">
<link rel="canonical" href="{url_attr}">
<script>location.replace({url_js});</script>
<style>body{{font-family:sans-serif;text-align:center;margin-top:20vh;color:#333}}a{{color:#0a58ca}}</style>
</head>
<body>
<p>動画へ移動します… / Redirecting to the video…</p>
<p><a href="{url_attr}">開かない場合はこちら / Tap here if it does not open</a></p>
</body>
</html>
"""

COMING = """<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>TOKI STAY 動画ガイド（準備中）</title>
<style>body{font-family:sans-serif;text-align:center;margin-top:20vh;color:#333}</style>
</head>
<body>
<p>この動画は準備中です。<br>This video is coming soon.</p>
</body>
</html>
"""


def main():
    with open(os.path.join(ROOT, "links.json"), encoding="utf-8") as f:
        links = json.load(f)
    count = 0
    for slug, url in links.items():
        folder = os.path.join(ROOT, slug)
        os.makedirs(folder, exist_ok=True)
        if url:
            page = TEMPLATE.format(
                url_attr=html.escape(url, quote=True),
                url_js=json.dumps(url),
            )
        else:
            page = COMING
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(page)
        count += 1
    # Jekyll 無効化（GitHub Pages で余計な処理をさせない）
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    print("built %d pages" % count)


if __name__ == "__main__":
    main()
