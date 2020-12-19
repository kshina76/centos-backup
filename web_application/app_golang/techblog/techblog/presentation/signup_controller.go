package presentation

import (
	//"database/sql"
	"crypto/rand"
	"net/http"
	"html/template"
	"time"
	"techblog/usecase"
	//"github.com/gorilla/mux"
	"fmt"
	//"strconv"
	"log"
)

type SignupPresentation interface {
	Signup(http.ResponseWriter, *http.Request)
	SignupView(http.ResponseWriter, *http.Request)
	Login(http.ResponseWriter, *http.Request)
	LoginView(http.ResponseWriter, *http.Request)
	AdminView(http.ResponseWriter, *http.Request)
}

type signupPresentation struct {
	signupUsecase usecase.SignupUsecase
}

func NewSignupPresentation(signupUsecase usecase.SignupUsecase) SignupPresentation {
	signupPresentation := new(signupPresentation)
	signupPresentation.signupUsecase = signupUsecase
	return signupPresentation
}

func (sp *signupPresentation) SignupView(writer http.ResponseWriter, request *http.Request) {
	t := template.Must(template.ParseFiles("templates/base.html", "templates/signup.html", "templates/sidebar.html"))
	t.ExecuteTemplate(writer, "base", nil)
}

func (sp *signupPresentation) LoginView(writer http.ResponseWriter, request *http.Request) {
	t := template.Must(template.ParseFiles("templates/base.html", "templates/login.html", "templates/sidebar.html"))
	t.ExecuteTemplate(writer, "base", nil)
}

func (sp *signupPresentation) AdminView(writer http.ResponseWriter, request *http.Request) {
	t := template.Must(template.ParseFiles("templates/base.html", "templates/admin.html", "templates/sidebar.html"))
	t.ExecuteTemplate(writer, "base", nil)
}

func (sp *signupPresentation) Signup(writer http.ResponseWriter, request *http.Request) {
	err := request.ParseForm()
	if err != nil {
		fmt.Println(err)
	}
	user := &usecase.Users{
		Uuid:		createUUID(),
		Name:		request.PostFormValue("name"),
		Email:		request.PostFormValue("email"),
		Password:	request.PostFormValue("password"),
		CreatedAt:	time.Now(),
	}
	err = sp.signupUsecase.CreateUser(user)
	if err != nil {
		fmt.Println(err)
	}
	http.Redirect(writer, request, "/", 301)
}

func (sp *signupPresentation) Login(writer http.ResponseWriter, request *http.Request) {
	user := &usecase.Users{
		Uuid:		createUUID(),
		Email:		request.PostFormValue("email"),
		Password:	request.PostFormValue("password"),
		CreatedAt:	time.Now(),
	}
	uuid, err := sp.signupUsecase.LoginUser(user)
	if err != nil {
		fmt.Println(err)
		http.Redirect(writer, request, "/login", 301)
	}
	cookie := http.Cookie{
		Name:		"_cookie",
		Value:		uuid,
		HttpOnly:	true,
	}
	http.SetCookie(writer, &cookie)
	http.Redirect(writer, request, "/admin", 301)
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
