package presentation

import (
	"net/http"
	"html/template"
	//"os"
)

func Login(writer http.ResponseWriter, request *http.Request) {
	t := template.Must(template.ParseFiles("templates/base.html", "templates/login.html", "templates/sidebar.html"))
	t.ExecuteTemplate(writer, "base", nil)
}