package presentation

import (
	"net/http"
	"html/template"
	"techblog/domain"
	//"log"
	"fmt"
)

func Signup(writer http.ResponseWriter, request *http.Request) {
	t := template.Must(template.ParseFiles("templates/base.html", "templates/signup.html", "templates/sidebar.html"))
	t.ExecuteTemplate(writer, "base", nil)
}

func SignupAccount(writer http.ResponseWriter, request *http.Request) {
	if err := request.ParseForm(); err != nil {
		fmt.Println("Cannot parse form.")
	}
	//domainインスタンス化、メソッド呼び出し
	user := domain.User{
		Name: request.PostFormValue("name"),
		Email: request.PostFormValue("email"),
		Password: request.PostFormValue("password"),
	}
	//userのメソッドを呼び出し
	if err := user.Create(); err != nil {
		//log.Fatal(err)
		fmt.Println("Cannot create user.")
	}
	//サインアップが完了したら、ログインページにリダイレクト
	http.Redirect(writer, request, "/login", 302)
}

func Login(writer http.ResponseWriter, request *http.Request) {
	t := template.Must(template.ParseFiles("templates/base.html", "templates/login.html", "templates/sidebar.html"))
	t.ExecuteTemplate(writer, "base", nil)
}

//認証処理。ログインできたらadminサイトにリダイレクト
func Authenticate(writer http.ResponseWriter, request *http.Request) {
	if err := request.ParseForm(); err != nil {
		fmt.Println("Cannot parse form.")
	}
	user, err := domain.UserByEmail(request.PostFormValue("email"))
	if err != nil {
		fmt.Println("Cannot find user.")
	}
	if user.Password == domain.Encrypt(request.PostFormValue("password")) {
		session, err := user.CreateSession()
		if err != nil {
			fmt.Println("Cannot create session.")
		}
		cookie := http.Cookie{
			Name:     "_cookie",
			Value:    session.Uuid,
			HttpOnly: true,
		}
		http.SetCookie(writer, &cookie)
		http.Redirect(writer, request, "/admin", 302)
	} else {
		http.Redirect(writer, request, "/login", 302)
	}
}

func Admin(writer http.ResponseWriter, request *http.Request) {
	_, err := session(writer, request)
	if err != nil {
		http.Redirect(writer, request, "/login", 302)
	} else {
		t := template.Must(template.ParseFiles("templates/base.html", "templates/admin.html", "templates/sidebar.html"))
		t.ExecuteTemplate(writer, "base", nil)
	}
}
