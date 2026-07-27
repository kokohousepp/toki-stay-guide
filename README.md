# TOKI STAY 動画ガイド 中継リンク

ハウスマニュアルのQR／リンクは、YouTube動画に**直接**ではなく、この中継URLに向ける。
動画を撮り直してYouTube URLが変わっても、**転送先を1行書き換えるだけ**でマニュアル側（印刷済みQR含む）は無変更。

## 固定URL一覧（マニュアルはこれを指す）

ベース: `https://kokohousepp.github.io/toki-stay-guide/`

| 種類 | スラッグ | 固定URL |
|------|---------|---------|
| 駅からのアクセス（共通） | `access` | https://kokohousepp.github.io/toki-stay-guide/access |
| エアコン（共通） | `aircon` | https://kokohousepp.github.io/toki-stay-guide/aircon |
| ゴミの分別・捨て方（共通） | `gomi` | https://kokohousepp.github.io/toki-stay-guide/gomi |
| 冷蔵庫（共通） | `fridge` | https://kokohousepp.github.io/toki-stay-guide/fridge |
| 電子レンジ（共通） | `microwave` | https://kokohousepp.github.io/toki-stay-guide/microwave |
| 洗濯機（共通） | `washer` | https://kokohousepp.github.io/toki-stay-guide/washer |
| 炊飯器（共通） | `ricecooker` | https://kokohousepp.github.io/toki-stay-guide/ricecooker |
| お風呂・給湯（共通） | `bath` | https://kokohousepp.github.io/toki-stay-guide/bath |
| 入室の流れ 403 | `403-entry` | https://kokohousepp.github.io/toki-stay-guide/403-entry |
| 入室の流れ 405 | `405-entry` | https://kokohousepp.github.io/toki-stay-guide/405-entry |

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
