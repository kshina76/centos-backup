# ベースとなるDockerイメージ指定
FROM golang:latest
# コンテナ内に作業ディレクトリを作成
RUN mkdir /go/src/techblog
# コンテナログイン時のディレクトリ指定
WORKDIR /go/src/techblog
# ホストのファイルをコンテナの作業ディレクトリに移行
COPY ./techblog /go/src/techblog
# golangでdbを操作するためのパッケージ
RUN go get github.com/lib/pq