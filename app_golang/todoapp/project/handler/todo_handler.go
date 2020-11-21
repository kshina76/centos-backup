package handler

import (
	"fmt"
	"html/template"
	"net/http"
	"project/usecase"
)

/*
handler層(presentation層)の構造体(クラス)を定義していく。
プロパティにはusecase層のinterfaceを埋め込む
*/
type TodoHandler struct {
	todoUsecase usecase.TodoUsecase
}

func NewTodoHandler(todoUsecase *usecase.TodoUsecase) TodoHandler {
	todoHandler := new(TodoHandler)
	todoHandler.todoUsecase = todoUsecase
	return todoHandler
}

/*
handler層(presentation層)のメソッドを定義していく
*/
func (todoHandler *TodoHandler) Index(writer http.ResponseWriter, request *http.Request) {
	if err := request.ParseForm(); != nil {
		fmt.Println("Cannot parse form")
	}
	data := new(usecase.TodoModel)
	data.Title = request.ParseFormValue("title")
	data.Status = request.ParseFormValue("status")

	//ユースケースを呼んで、データを取得する
	tm, err := todoHandler.todoUsecase.AddTodo(data)

	fmt.Println(tm)

	//テンプレートエンジンを呼んで、「テンプレート」と「ユースケースで取得したデータ」をレンダリングする
	t := template.Must(template.ParseFiles("templates/base.html", "templates/content.html"))
	t.ExecuteTemplate(writer, "base", nil)
}

