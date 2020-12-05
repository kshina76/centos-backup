# ベースとなるDockerイメージ指定
FROM golang:latest
# コンテナ内に作業ディレクトリを作成
RUN mkdir /go/src/atcoder
# コンテナログイン時のディレクトリ指定
WORKDIR /go/src/atcoder
# golangのvscodeのパッケージ依存
RUN go get github.com/mdempsky/gocode \
           github.com/ramya-rao-a/go-outline \
           github.com/uudashr/gopkgs/v2/cmd/gopkgs
