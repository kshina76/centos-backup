package usecase

import (
	"time"
	"techblog/infra"
	"database/sql"
	"errors"
	"crypto/rand"
	"log"
	"fmt"
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

type Session struct {
	Id			int
	Uuid		string
	Email		string
	CreatedAt	time.Time
}

var ErrPassword = "do not match password"

type SignupUsecase interface {
	CreateUser(*Users) (error)
	LoginUser(*Users) (string, error)
}

type signupUsecase struct {
	signupInfra infra.SignupInfra   //signup
	sessionInfra infra.SessionInfra //session
}

func NewSignupUsecase(signupInfra infra.SignupInfra, sessionInfra infra.SessionInfra) SignupUsecase {
	signupUsecase := new(signupUsecase)
	signupUsecase.signupInfra = signupInfra
	signupUsecase.sessionInfra = sessionInfra
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

//LoginUser is exposed
func (su *signupUsecase) LoginUser(users *Users) (string, error) {
	userDTO, err := su.signupInfra.FindUserByEmail(users.Email)
	sessionDTO := &infra.SessionDTO{}
	if err != nil {
		return "", err
	}
	if users.Password != userDTO.Password {
		return "", errors.New(ErrPassword)
	}
	sessionDTO.Uuid = createUUID()
	sessionDTO.Email = users.Email
	sessionDTO.CreatedAt = users.CreatedAt
	err = su.sessionInfra.Create(sessionDTO)
	if err != nil {
		return "", err
	}
	return sessionDTO.Uuid, err
}

//util func
func createUUID() (uuid string) {
	u := new([16]byte)
	_, err := rand.Read(u[:])
	if err != nil {
		log.Fatalln("Cannot generate UUID", err)
	}

	// 0x40 is reserved variant from RFC 4122
	u[8] = (u[8] | 0x40) & 0x7F
	// Set the four most significant bits (bits 12 through 15) of the
	// time_hi_and_version field to the 4-bit version number.
	u[6] = (u[6] & 0xF) | (0x4 << 4)
	uuid = fmt.Sprintf("%x-%x-%x-%x-%x", u[0:4], u[4:6], u[6:8], u[8:10], u[10:])
	return
}
