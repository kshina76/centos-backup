# ベースとなるDockerイメージ指定
FROM golang:latest
# コンテナ内に作業ディレクトリを作成
RUN mkdir /go/src/project
# コンテナログイン時のディレクトリ指定
WORKDIR /go/src/project
# ホストのファイルをコンテナの作業ディレクトリに移行
#COPY ./techblog /go/src/techblog
# golangでdbを操作するためのパッケージ
RUN go get github.com/lib/pq

# rubyをインストール(sassを使うために必要)
# ruby-devはgemでのエラー回避
RUN apt update && apt install -y ruby ruby-dev
RUN gem install sass