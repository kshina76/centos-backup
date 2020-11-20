package main

import (
	"net/http"
	//"html/template"
	"project/handler"
)

func main() {
	mux := http.NewServeMux()

	//静的ファイルの設定
	files := http.FileServer(http.Dir("static"))
	mux.Handle("/static/", http.StripPrefix("/static/", files))

	//トップページ
	mux.HandleFunc("/", handler.Index)

	//サーバ起動
	server := &http.Server {
		Addr: "0.0.0.0:8080",
		Handler: mux,
	}
	server.ListenAndServe()
}