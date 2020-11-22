package usecase

import (
	//"html/template"
	"time"
	"project/infra"
	"fmt"
)

type TodoModel struct {
	Id		int
	Title	string
	Status	string
	Date	time.Time
}

type TodoUsecase interface {
	AddTodo(*TodoModel) error
	GetAll() error
}

type todoUsecase struct {
	todoInfra infra.TodoInfra
}

func NewTodoUsecase(todoInfra infra.TodoInfra) TodoUsecase {
	todoUsecase := new(todoUsecase)
	todoUsecase.todoInfra = todoInfra
	return todoUsecase
}

func (tu *todoUsecase) AddTodo(tm *TodoModel) (err error) {
	tmd := new(infra.TodoModelDTO)
	tmd.Title = tm.Title
	tmd.Status = tm.Status
	_, err = tu.todoInfra.Insert(tmd)
	return
}

func (tu *todoUsecase) GetAll() (err error) {
	todos, err := tu.todoInfra.FindAll()
	fmt.Println(todos)
	return
}