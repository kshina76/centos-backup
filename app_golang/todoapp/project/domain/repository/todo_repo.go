package repository

import (
	"project/model"  //引数でmodel.TodoModelを渡しておくと、DBに保存するときにプロパティの値をそのまま使える
)

type TodoRepository interface {
	//FindAll()
	//Find
	Insert(todo *model.TodoModel) (*model.TodoModel, error)  //引数でmodel.TodoModelを渡しておくと、DBに保存するときにプロパティの値をそのまま使える
	//Delete()
	//Putは、DeleteとInsertを組み合わせればいいかな？
}