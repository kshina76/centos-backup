package handler

import (
	"fmt"
	"html/template"
	"net/http"
	"project/usecase"
)

type TodoHandler interface {
	//Index(http.ResponseWriter, *http.Request)
	Todo(http.ResponseWriter, *http.Request)
}

/*
handler層(presentation層)の構造体(クラス)を定義していく。
プロパティにはusecase層のinterfaceを埋め込む
interfaceで見えなくするので、構造体の最初の文字は小文字にして大丈夫(interface経由でアクセスするから)
*/
type todoHandler struct {
	todoUsecase usecase.TodoUsecase
}

func NewTodoHandler(todoUsecase usecase.TodoUsecase) TodoHandler {
	todoHandler := new(todoHandler)
	todoHandler.todoUsecase = todoUsecase
	return todoHandler
}

func (th *todoHandler) Todo(writer http.ResponseWriter, request *http.Request) {
	err := request.ParseForm()
	if err != nil {
		fmt.Println("Cannot parse form")
	}
	err = th.todoUsecase.GetAll()  //test中なのでerrしか返していない
	if err != nil {
		fmt.Println(err)
	}
	switch request.Method {
	case "GET":
		t := template.Must(template.ParseFiles("templates/base.html", "templates/content.html"))
		t.ExecuteTemplate(writer, "base", nil)
	case "POST":
		data := new(usecase.TodoModel)
		data.Title = request.FormValue("title")
		data.Status = request.FormValue("status")
		err = th.todoUsecase.AddTodo(data)
		if err != nil {
			fmt.Println(err)
		}
		t := template.Must(template.ParseFiles("templates/base.html", "templates/content.html"))
		t.ExecuteTemplate(writer, "base", nil)
	}
}