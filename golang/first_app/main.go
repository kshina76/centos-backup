package main

import (
	"net/http"
)

func main() {

	/*静的コンテンツ
	- StripPrefixはリクエストURLの先頭から指定された文字列を削除する
		- http://localhost/static/css/style.css にアクセスが来たら、「<アプリケーションルート>/css/style.css」のファイルを探す
			- 今回は/publicがアプリケーションルート
	*/
	mux := http.NewServeMux()
	files := http.FileServer(http.Dir("/public"))
	mux.Handle("/static/", http.StripPrefix("/static/", files))

	//URLルーティング
	mux.HandleFunc("/", index)
	// error
	mux.HandleFunc("/err", err)

	// defined in route_auth.go
	mux.HandleFunc("/login", login)
	mux.HandleFunc("/logout", logout)
	mux.HandleFunc("/signup", signup)
	mux.HandleFunc("/signup_account", signupAccount)
	mux.HandleFunc("/authenticate", authenticate)

	// defined in route_thread.go
	mux.HandleFunc("/thread/new", newThread)
	mux.HandleFunc("/thread/create", createThread)
	mux.HandleFunc("/thread/post", postThread)
	mux.HandleFunc("/thread/read", readThread)

	//サーバの設定
	server := &http.Server() {
		Addr: "0.0.0.0:8000", 
		Handler: mux
	}

	//サーバを立てる
	server.ListenAndServe()
}