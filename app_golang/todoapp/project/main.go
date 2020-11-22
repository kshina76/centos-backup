package main

import (
	"net/http"
	"project/handler"
	"project/usecase"
	"project/infra"
)

/*
type TestStruct struct {
	Id int
	name string
}
*/

func main() {
	//DI
	sh := infra.NewSqlHandler()
	ti := infra.NewTodoInfra(sh)
	tu := usecase.NewTodoUsecase(ti)
	th := handler.NewTodoHandler(tu)

	//マルチプレクサの定義
	mux := http.NewServeMux()

	//静的ファイルの設定
	files := http.FileServer(http.Dir("static"))
	mux.Handle("/static/", http.StripPrefix("/static/", files))

	//トップページ
	mux.HandleFunc("/todo", th.Todo)
	//mux.HandleFunc("/")

	//サーバ起動
	server := &http.Server {
		Addr: "0.0.0.0:8080",
		Handler: mux,
	}
	server.ListenAndServe()
	

}