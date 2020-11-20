package model

import (
	"time"
)

type TodoModel struct {
	Id		int
	Title	string
	Status	string
	Date	time.Time
}