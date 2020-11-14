package main

import (
	"fmt"
	"net/http"
	//"html/template"
	"techblog/view"
)

func main() {
	mux := http.NewServeMux()

	//静的ファイルの設定
	files := http.FileServer(http.Dir("static"))
	mux.Handle("/static/", http.StripPrefix("/static/", files))

	mux.HandleFunc("/", view.Index)
	mux.HandleFunc("/login", view.Login)

	server := &http.Server {
		Addr: "0.0.0.0:8080",
		Handler: mux,
	}
	server.ListenAndServe()
}

func index(writer http.ResponseWriter, request *http.Request) {
	fmt.Fprintf(writer, "Hello")
}