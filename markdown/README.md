# markdownで資料を作る系のまとめ

## markdownからいい感じのPDF資料を作成する

### pdf作成
- tocがいらないなら外すとか適宜自分の環境に合わせる
- dockerhubからイメージはpullされてくるので、いきなり以下のコマンドを実行していい


```
docker run --rm -v $(pwd -W):/data frozenbonito/pandoc-eisvogel-ja:plantuml \
    --listings \
    -N \
    --toc \
    -V linkcolor=blue \
    -V table-use-row-colors=true \
    -V titlepage=true \
    -V toc-own-page=true \
    -V toc-title="目次" \
    -o doc.pdf \
    example-pandoc-eisvogel-ja.md
```

### 入力サンプル
- yaml meta blockというものをページの最初に記述するのを忘れずに

```markdown
---
title: 使用例
subtitle: サブタイトル
date: 2020-05-07
author: test
---

# 概要

日本語で書いた Markdown を PDF に変換できます。

# 見出しサンプル

## 見出し 2

### 見出し 3

# 各記法のサンプル

## 箇条書きリスト

- アイテム 1
- アイテム 2
- アイテム 3
  - アイテム 3-1
    - アイテム 3-1-1

## 番号付きリスト

1. アイテム 1
1. アイテム 2
1. アイテム 3
   1. アイテム 3-1
      1. アイテム 3-1-1

## 引用

> 引用です。
>
> > 二重引用です。

## リンク

[Eisvogel template](https://github.com/Wandmalfarbe/pandoc-latex-template) を使っています。

## テーブル

| 左寄せ | 中央 | 右寄せ |
| :----- | ---- | -----: |
| い     | ろ   |     は |
| に     | ほ   |     へ |

```

### 参考文献
- https://qiita.com/frozenbonito/items/10a38c5fd4ba97a9bef0
- https://hub.docker.com/r/frozenbonito/pandoc-eisvogel-ja
- https://github.com/frozenbonito/docker-pandoc-eisvogel-ja
- https://gist.githubusercontent.com/frozenbonito/eb2511a0f5812bc0d418dc5d5dffad72/raw/fe1a2dc1e293325e7610dc65d1fe3cae92799fa7/example-pandoc-eisvogel-ja.md
