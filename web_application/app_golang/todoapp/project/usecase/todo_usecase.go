package usecase

import (
	//"html/template"
	"time"
	"project/infra"
	//"fmt"
)

type TodoModel struct {
	Id		int
	Title	string
	Status	string
	Date	time.Time
}

type TodoUsecase interface {
	AddTodo(*TodoModel) error
	GetAll() ([]*TodoModel, error)
	UpdateTodo(*TodoModel) error
	DeleteTodo(*TodoModel) error 
}

type todoUsecase struct {
	todoInfra infra.TodoInfra
	//transaction scriptでは、ここにDAOだけを定義するっぽい。DTOはここに書かない(インスタンス変数としない)
	//DAOとは、DAO自体はデータを保持せず、DBにアクセスし、DTO/VOを返すもの
}

func NewTodoUsecase(todoInfra infra.TodoInfra) TodoUsecase {
	todoUsecase := new(todoUsecase)
	todoUsecase.todoInfra = todoInfra
	return todoUsecase
}

func (tu *todoUsecase) AddTodo(tm *TodoModel) (err error) {
	tmd := new(infra.TodoModelDTO)
	tmd.Id = tm.Id
	tmd.Title = tm.Title
	tmd.Status = tm.Status
	_, err = tu.todoInfra.Insert(tmd)
	return
}

func (tu *todoUsecase) GetAll() (tmds []*TodoModel, err error) {
	todos, err := tu.todoInfra.FindAll()
	for _, t := range todos{
		tmd := new(TodoModel)
		tmd.Id = t.Id
		tmd.Title = t.Title
		tmd.Status = t.Status
		tmds = append(tmds, tmd)
	}
	return
}

func (tu *todoUsecase) UpdateTodo(tm *TodoModel) error {
	tmd := new(infra.TodoModelDTO)
	tmd.Id = tm.Id
	tmd.Title = tm.Title
	tmd.Status = tm.Status
	err := tu.todoInfra.Update(tmd)
	return err
}

func (tu *todoUsecase) DeleteTodo(tm *TodoModel) error {
	tmd := new(infra.TodoModelDTO)
	tmd.Id = tm.Id
	err := tu.todoInfra.Delete(tmd)
	return err
}

//改善点として、DTOとmodelを変換するユーティリティ関数を作ったほうがいいかもしれない