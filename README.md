# TOKI STAY 動画ガイド 中継リンク

ハウスマニュアルのQR／リンクは、YouTube動画に**直接**ではなく、この中継URLに向ける。
動画を撮り直してYouTube URLが変わっても、**転送先を1行書き換えるだけ**でマニュアル側（印刷済みQR含む）は無変更。

## 固定URL一覧（マニュアルはこれを指す）

ベース: `https://kokohousepp.github.io/toki-stay-guide/`

| 種類 | スラッグ | 固定URL |
|------|---------|---------|
| 駅からのアクセス（共通） | `access` | https://kokohousepp.github.io/toki-stay-guide/access |
| エントランス オートロック解除（共通） | `entrance` | https://kokohousepp.github.io/toki-stay-guide/entrance |
| ゴミの分別・捨て方（共通） | `gomi` | https://kokohousepp.github.io/toki-stay-guide/gomi |
| 冷蔵庫（共通） | `fridge` | https://kokohousepp.github.io/toki-stay-guide/fridge |
| ガスコンロ（共通） | `stove` | https://kokohousepp.github.io/toki-stay-guide/stove |
| 炊飯器（共通） | `ricecooker` | https://kokohousepp.github.io/toki-stay-guide/ricecooker |
| 電気ケトル（共通） | `kettle` | https://kokohousepp.github.io/toki-stay-guide/kettle |
| お風呂・給湯（共通） | `bath` | https://kokohousepp.github.io/toki-stay-guide/bath |
| キーボックス〜お部屋の入室 403 | `403-room` | https://kokohousepp.github.io/toki-stay-guide/403-room |
| エアコン 403 | `403-aircon` | https://kokohousepp.github.io/toki-stay-guide/403-aircon |
| 電子レンジ 403 | `403-microwave` | https://kokohousepp.github.io/toki-stay-guide/403-microwave |
| 洗濯機 403 | `403-washer` | https://kokohousepp.github.io/toki-stay-guide/403-washer |
| キーボックス〜お部屋の入室 405 | `405-room` | https://kokohousepp.github.io/toki-stay-guide/405-room |
| エアコン 405 | `405-aircon` | https://kokohousepp.github.io/toki-stay-guide/405-aircon |
| 電子レンジ 405 | `405-microwave` | https://kokohousepp.github.io/toki-stay-guide/405-microwave |
| 洗濯機 405 | `405-washer` | https://kokohousepp.github.io/toki-stay-guide/405-washer |
| 駅からの道順 フクシア202 | `202-access` | https://kokohousepp.github.io/toki-stay-guide/202-access |
| キーボックス〜エントランス 202 | `202-checkin` | https://kokohousepp.github.io/toki-stay-guide/202-checkin |
| 鍵の使い方・お部屋の入室 202 | `202-room` | https://kokohousepp.github.io/toki-stay-guide/202-room |
| エアコン 202 | `202-aircon` | https://kokohousepp.github.io/toki-stay-guide/202-aircon |
| お風呂・給湯 202 | `202-bath` | https://kokohousepp.github.io/toki-stay-guide/202-bath |
| 洗濯機 202 | `202-washer` | https://kokohousepp.github.io/toki-stay-guide/202-washer |
| ガスコンロ 202 | `202-stove` | https://kokohousepp.github.io/toki-stay-guide/202-stove |
| 電子レンジ 202 | `202-microwave` | https://kokohousepp.github.io/toki-stay-guide/202-microwave |
| 電気ケトル 202 | `202-kettle` | https://kokohousepp.github.io/toki-stay-guide/202-kettle |
| 炊飯器 202 | `202-ricecooker` | https://kokohousepp.github.io/toki-stay-guide/202-ricecooker |
| ゴミの分別・捨て方 202 | `202-gomi` | https://kokohousepp.github.io/toki-stay-guide/202-gomi |

※フクシア202は別建物のため【共通】スラッグを使わず、全て `202-` 付きの部屋別スラッグ（2026-09-23 追加。現在は仮動画＝タイトルカード）。
※まだ動画が無いスラッグは「準備中 / Coming soon」ページを表示（QRは失効しない）。

## 動画リンクを設定・差し替える（どちらのMacでも）

```bash
cd "$HOME/ドキュメント/toki-stay-guide"
./update.sh washer https://youtu.be/xxxxxxxxxxx
```

これだけで links.json 更新 → ページ再生成 → GitHubへpush まで自動。反映は数十秒〜1分。

手動でやる場合:
1. `links.json` の該当スラッグのURLを書き換え
2. `python3 build.py`
3. `git add -A && git commit -m "update link" && git push`

## 仕組み

- `links.json` … スラッグ → 現在のYouTube URL（元データ）
- `build.py` … 各スラッグに転送用 `index.html` を生成（meta refresh + JS）
- 各 `index.html` は検索避け（noindex）。GitHub Pages が静的配信

## 注意

- YouTube動画は**限定公開（unlisted）**・コメントオフのまま
- 動画に**キーボックス暗証番号・Wi-Fiパスワードを映さない**（この中継URLは公開されているため）
