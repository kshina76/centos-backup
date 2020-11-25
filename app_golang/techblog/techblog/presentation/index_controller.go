package presentation

import(
	"net/http"
	"html/template"
	"time"
)

//Posts struct is exposed, this is mock data
type Posts struct {
	Title		string
	Name		string
	Text		string
	Tag			[]string
	Category	string
	CreatedAt	time.Time
}

//Index function is exposed
func Index(writer http.ResponseWriter, request *http.Request) {
	//mock data
	post1 := Posts{
		Title:		"mock title1",
		Name:		"Kosuke",
		Text:		"this is test comment part1.",
		Tag:		[]string{"tag1", "tag2"},
		Category:	"python",
		CreatedAt:	time.Now(),
	}
	post2 := Posts{
		Title:		"mock title2",
		Name:		"Peyonjun",
		Text:		"this is test comment part2, anyohaseyo.",
		Tag:		[]string{"tag1", "tag2", "tag3"},
		Category:	"go",
		CreatedAt:	time.Now(),
	}
	var posts = []Posts{}
	posts = append(posts, post1)
	posts = append(posts, post2)

	t := template.Must(template.ParseFiles("templates/base.html", "templates/article.html", "templates/sidebar.html"))
	t.ExecuteTemplate(writer, "base", posts)
}

//Detail function is exposed
func Detail(writer http.ResponseWriter, request *http.Request) {
	//mock data
	post1 := Posts{
		Title:		"mock title1",
		Name:		"Kosuke",
		Text:		"this is test comment part1.",
		Tag:		[]string{"tag1", "tag2"},
		Category:	"python",
		CreatedAt:	time.Now(),
	}

	t := template.Must(template.ParseFiles("templates/base.html", "templates/detail.html", "templates/sidebar.html"))
	t.ExecuteTemplate(writer, "base", post1)
}
