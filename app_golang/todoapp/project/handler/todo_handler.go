package handler

import (
	"fmt"
	"html/template"
	"net/http"
	"project/usecase"
	"github.com/gorilla/mux"
	"strconv"
)

type TodoHandler interface {
	Todo(http.ResponseWriter, *http.Request)
	Edit(http.ResponseWriter, *http.Request)
	Delete(http.ResponseWriter, *http.Request)
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
	switch request.Method {
	case "GET":
		tmds, err := th.todoUsecase.GetAll()
		if err != nil {
			fmt.Println(err)
		}
		t := template.Must(template.ParseFiles("templates/base.html", "templates/content.html"))
		t.ExecuteTemplate(writer, "base", tmds)
	case "POST":
		data := new(usecase.TodoModel)
		data.Title = request.FormValue("title")
		data.Status = request.FormValue("status")
		err = th.todoUsecase.AddTodo(data)
		if err != nil {
			fmt.Println(err)
		}
		tmds, err := th.todoUsecase.GetAll()
		if err != nil {
			fmt.Println(err)
		}
		t := template.Must(template.ParseFiles("templates/base.html", "templates/content.html"))
		t.ExecuteTemplate(writer, "base", tmds)
	}
}

func (th *todoHandler) Edit(writer http.ResponseWriter, request *http.Request) {
	//GetTodoByIDを使用して、選択されたIdのtodoだけを取得する
	//executetemplateにそのtodoを入れる
	//htmlでformの行き先にidを指定しているから、gorilla.muxに戻るとpostでgorillaのvarからidを取得できるから、そこから書き換える
	vars := mux.Vars(request)
	switch request.Method {
	case "GET":
		//tmd, err := th.todoUsecase.GetTodoById(vars["id"])
		t := template.Must(template.ParseFiles("templates/base.html", "templates/edit.html"))
		t.ExecuteTemplate(writer, "base", vars["id"])
	case "POST":
		data := new(usecase.TodoModel)
		data.Id, _ = strconv.Atoi(vars["id"]) 
		data.Title = request.FormValue("title")
		data.Status = request.FormValue("status")
		err := th.todoUsecase.UpdateTodo(data)
		if err != nil {
			fmt.Println(err)
		}
		http.Redirect(writer, request, "/todo", 301)
	}
}

func (th *todoHandler) Delete(writer http.ResponseWriter, request *http.Request) {
	vars := mux.Vars(request)
	switch request.Method {
	case "GET":
		t := template.Must(template.ParseFiles("templates/base.html", "templates/delete.html"))
		t.ExecuteTemplate(writer, "base", vars["id"])
	case "POST":
		fmt.Println("test")
		data := new(usecase.TodoModel)
		data.Id, _ = strconv.Atoi(vars["id"])
		err := th.todoUsecase.DeleteTodo(data)
		if err != nil {
			fmt.Println(err)
		}
		http.Redirect(writer, request, "/todo", 301)
	}
}