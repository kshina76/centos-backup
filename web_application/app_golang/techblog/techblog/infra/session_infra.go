package infra

import (
	"time"
	"fmt"
)

//SessionDTO is exposed
type SessionDTO struct {
	Id			int
	Uuid		string
	Email		string
	CreatedAt	time.Time
}

//SessionInfra is exposed
type SessionInfra interface {
	Create(*SessionDTO) (error)
	FindSessionByEmail(*SessionDTO) (*SessionDTO, error)
}

type sessionInfra struct {}

//NewSessionInfra is exposed
func NewSessionInfra() SessionInfra {
	return &sessionInfra{}
}

//Create is exposed
func (si *sessionInfra) Create(sessionDTO *SessionDTO) (err error) {
	statement := "insert into sessions (uuid, email, created_at) "
	statement += "values ($1, $2, $3) returning id"
	stmt, err := Db.Prepare(statement)
	defer stmt.Close()
	err = stmt.QueryRow(sessionDTO.Uuid, sessionDTO.Email, sessionDTO.CreatedAt).Scan(&sessionDTO.Id)
	if err != nil {
		return
	}
	return
}

//FindSessionByEmail is exposed
func (si *sessionInfra) FindSessionByEmail(sessionDTO *SessionDTO) (*SessionDTO, error) {
	query := "select * from sessions where uuid = $1"
	err := Db.QueryRow(query, sessionDTO.Uuid).Scan(&sessionDTO.Id, &sessionDTO.Uuid, &sessionDTO.Email, &sessionDTO.CreatedAt)
	if err != nil {
		return sessionDTO, err
	}
	return sessionDTO, err
}

//Delete is exposed
func (si *sessionInfra) Delete(sessionDTO *SessionDTO) (err error) {
	query := "delete from sessions where uuid = $1"
	result, err := Db.Exec(query, sessionDTO.Uuid)
	fmt.Println(result)
	if err != nil {
		return
	}
	return
}
