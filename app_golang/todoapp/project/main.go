package main

import (
	"net/http"
	"project/handler"
	"project/usecase"
	"project/infra"
	"github.com/gorilla/mux"
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
	//mux := http.NewServeMux()
	r := mux.NewRouter()

	//静的ファイルの設定
	files := http.FileServer(http.Dir("static"))
	r.Handle("/static/", http.StripPrefix("/static/", files))

	//トップページ
	r.HandleFunc("/todo", th.Todo)
	r.HandleFunc("/edit/{id:[0-9]+}", th.Edit)
	r.HandleFunc("/delete/{id:[0-9]+}", th.Delete)

	//サーバ起動
	server := &http.Server {
		Addr: "0.0.0.0:8080",
		Handler: r,
	}
	server.ListenAndServe()


}
