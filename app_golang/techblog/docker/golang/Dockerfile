# ベースとなるDockerイメージ指定
FROM golang:latest
# コンテナ内に作業ディレクトリを作成
RUN mkdir /go/src/techblog
# コンテナログイン時のディレクトリ指定
WORKDIR /go/src/techblog
# ホストのファイルをコンテナの作業ディレクトリに移行
#COPY ./techblog /go/src/techblog
# golangでdbを操作するためのパッケージ
RUN go get github.com/lib/pq \
           github.com/gorilla/mux

# golangのvscodeのパッケージ依存
RUN go get github.com/mdempsky/gocode \
           github.com/ramya-rao-a/go-outline \
           github.com/uudashr/gopkgs/v2/cmd/gopkgs

# rubyをインストール(sassを使うために必要)
# ruby-devはgemでのエラー回避
RUN apt update && apt install -y ruby ruby-dev
RUN gem install sass
