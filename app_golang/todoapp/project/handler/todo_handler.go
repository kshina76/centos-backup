package handler

import (
	"html/template"
	"net/http"
	//"project/usecase"
)

/*
handler層(presentation層)の構造体(クラス)を定義していく。
プロパティにはusecase層のinterfaceを埋め込む
*/
type TodoHandler struct {
	todoUsecase usecase.TodoUsecase
}

/*
handler層(presentation層)のメソッドを定義していく
*/
func (todoHandler *TodoHandler) Index(writer http.ResponseWriter, request *http.Request) {
	//ユースケースを呼んで、データを取得する

	//テンプレートエンジンを呼んで、「テンプレート」と「ユースケースで取得したデータ」をレンダリングする
	t := template.Must(template.ParseFiles("templates/base.html", "templates/content.html"))
	t.ExecuteTemplate(writer, "base", nil)
}

