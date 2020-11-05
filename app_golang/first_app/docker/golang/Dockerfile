# ベースとなるDockerイメージ指定
FROM golang:latest
# コンテナ内に作業ディレクトリを作成
RUN mkdir /go/src/chitchat
# コンテナログイン時のディレクトリ指定
WORKDIR /go/src/chitchat
# ホストのファイルをコンテナの作業ディレクトリに移行
COPY ./chitchat /go/src/chitchat
# golangでdbを操作するためのパッケージ
RUN go get github.com/lib/pq