package usecase

import (
	"html/template"
	"time"
	"project/infra"
)

type TodoModel struct {
	Id		int
	Title	string
	Status	string
	Date	time.Time
}

type TodoUsecase interface {
	AddTodo(*TodoModel) error
}

type todoUsecase struct {
	todoInfra infra.TodoInfra
}

func NewTodoUsecase(todoInfra *infra.TodoInfra) TodoUsecase {
	todoUsecase := new(todoUsecase)
	todoUsecase.todoInfra = todoInfra
	return todoUsecase
}

func (tu *todoUsecase) AddTodo(tm *TodoModel) (tm *TodoModel err error) {
	tm, err = tu.todoInfra.Insert(tm)
	return
}