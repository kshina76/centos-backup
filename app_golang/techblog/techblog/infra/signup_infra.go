package infra

import (
	"github.com/lib/pq"
	"time"
	//"fmt"
)

//SessionDTO is exposed
type SessionDTO struct {
	Id			int
	Uuid		string
	Email		string
	CreatedAt	time.Time
}

//User is exposed
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
}

type signupInfra struct {}

//NewSignupInfra is constracta
func NewSignupInfra() SignupInfra {
	signupInfra := new(signupInfra)
	return signupInfra
}

//Create is exposed
func (si *signupInfra) Create(user *UserDTO) (err error) {
	
}
