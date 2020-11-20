package usecase

import (
	"http/template"
)

/*
usecase層のinterfaceを定義する
*/
type TodoUsecase interface {
}

/*
domain層のrepositoryとserviceのinterfaceを定義する
*/
type todoUsecase struct {
	todoRepository TodoRepository
}