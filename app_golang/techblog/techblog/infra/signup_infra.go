package infra

import (
	//"github.com/lib/pq"
	"time"
	//"fmt"
)

//UserDTO is exposed
type UserDTO struct {
	Id			int
	Uuid		string
	Name		string
	Email		string
	Password	string
	CreatedAt	time.Time
}

//SignupInfra is exposed
type SignupInfra interface {
	Create(*UserDTO) error
	FindUserByEmail(string)  (*UserDTO, error)
}

type signupInfra struct {}

//NewSignupInfra is constracta
func NewSignupInfra() SignupInfra {
	signupInfra := new(signupInfra)
	return signupInfra
}

//Create is exposed
func (si *signupInfra) Create(userDTO *UserDTO) (err error) {
	statement := "insert into users (uuid, name, email, password, created_at) "
	statement += "values ($1, $2, $3, $4, $5) returning id"
	stmt, err := Db.Prepare(statement)
	defer stmt.Close()
	err = stmt.QueryRow(userDTO.Uuid, userDTO.Name, userDTO.Email, userDTO.Password, userDTO.CreatedAt).Scan(&userDTO.Id)
	if err != nil {
		return
	}
	return
}

//FindUserByEmail is exposed
func (si *signupInfra) FindUserByEmail(email string) (userDTO *UserDTO, err error) {
	query := "select * from users where email = $1"
	userDTO = &UserDTO{}
	err = Db.QueryRow(query, email).Scan(&userDTO.Id, &userDTO.Uuid, &userDTO.Name, &userDTO.Email, &userDTO.Password, &userDTO.CreatedAt)
	if err != nil {
		return
	}
	return
}
