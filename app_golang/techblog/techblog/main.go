package main

import (
	"net/http"
	//"html/template"
	"techblog/presentation"
)

func main() {
	mux := http.NewServeMux()

	//静的ファイルの設定
	files := http.FileServer(http.Dir("static"))
	mux.Handle("/static/", http.StripPrefix("/static/", files))

	//トップページ
	mux.HandleFunc("/", presentation.ListPosts)

	//詳細ページ
	mux.HandleFunc("/detail", presentation.DetailPost)

	//アカウント作成
	//mux.HandleFunc("/signup", presentation.Signup)
	//mux.HandleFunc("/signup-account", presentation.SignupAccount)

	//ログイン
	//mux.HandleFunc("/login", presentation.Login)
	//mux.HandleFunc("/authenticate", presentation.Authenticate)

	//mux.HandleFunc("/admin", presentation.Admin)
	//mux.HandleFunc("/post-article", presentation.PostArticle)

	//サーバ起動
	server := &http.Server {
		Addr: "0.0.0.0:8080",
		Handler: mux,
	}
	server.ListenAndServe()
}
