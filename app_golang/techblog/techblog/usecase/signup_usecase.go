package usecase

import (
	"time"
	"techblog/infra"
	"database/sql"
	//"fmt"
)

type Users struct {
	Id			int
	Uuid		string
	Name		string
	Email		string
	Password	string
	CreatedAt	time.Time
}

type SignupUsecase interface {
	CreateUser(*Users) (error)
}

type signupUsecase struct {
	signupInfra infra.SignupInfra
}

func NewSignupUsecase(signupInfra infra.SignupInfra) SignupUsecase {
	signupUsecase := new(signupUsecase)
	signupUsecase.signupInfra = signupInfra
	return signupUsecase
}

//CreateUser is exposed
func (su *signupUsecase) CreateUser(users *Users) (err error) {
	user, err := su.signupInfra.FindUserByEmail(users.Email)
	if err != nil {
		if err != sql.ErrNoRows {
			return
		}
	}
	//ユーザがすでに存在したらreturn
	if user.Id != 0 {
		return
	}
	userDTO := &infra.UserDTO{
		Id:			users.Id,
		Uuid:		users.Uuid,
		Name:		users.Name,
		Email:		users.Email,
		Password:	users.Password,
		CreatedAt:	users.CreatedAt,
	}
	err = su.signupInfra.Create(userDTO)
	if err != nil {
		return
	}
	return
}
