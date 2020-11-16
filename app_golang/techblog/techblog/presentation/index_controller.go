package presentation

import (
	"net/http"
	"html/template"
	//"os"
)

type Test struct {
	Name string
	Text string
}

func Index(writer http.ResponseWriter, request *http.Request) {
	t := template.Must(template.ParseFiles("templates/base.html", "templates/article.html", "templates/sidebar.html"))
	
	test1 := Test{
		Name: "Kosuke",
		Text: "dagnraeirgnaofinabfdb",
	}
	test2 := Test{
		Name: "Keisuke",
		Text: "svsdvsdvsv",
	}

	test := []Test{test1, test2}

	/*
	三つ目の引数を「base」が定義されたHTMLテンプレートに渡すことで、テンプレート内で値を使うことができる
	注意する点としては、値は「base」にしか渡されない。
	他のテンプレートに伝搬させたい時は、baseから他のテンプレートを呼ぶときに{{ template "content" . }}のように「.」をつける必要がある
	*/
	t.ExecuteTemplate(writer, "base", test)
}