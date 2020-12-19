package presentation

import (
	//"techblog/domain"
	"net/http"
	"fmt"
)

func PostArticle(writer http.ResponseWriter, request *http.Request) {
	sess, err := session(writer, request)
	if err != nil {
		http.Redirect(writer, request, "/login", 302)
	} else {
		err = request.ParseForm()
		if err != nil {
			fmt.Println("Cannot parse form.")
		}
		user, err := sess.User()
		if err != nil {
			fmt.Println("Cannot get user from session.")
		}
		title := request.PostFormValue("title")
		body := request.PostFormValue("body")
		//uuid := request.PostFormValue("uuid")
		if _, err := user.CreatePost(title, body); err != nil {
			fmt.Println("Cannot create post")
		}
		//url := fmt.Sprint("/t/read?id=", uuid)
		http.Redirect(writer, request, "/", 302)
	}
}