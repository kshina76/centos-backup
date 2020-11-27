package presentation

import(
	"net/http"
	"html/template"
	"time"
	//test
	"techblog/infra"
	"fmt"
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

//Test is used by infra-layer test
//type Test struct {}

//ListPosts function is exposed
func ListPosts(writer http.ResponseWriter, request *http.Request) {
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

//DetailPost function is exposed
func DetailPost(writer http.ResponseWriter, request *http.Request) {
	//mock data(user input)
	post1 := Posts{
		Title:		"mock title1",
		Name:		"Kosuke",
		Text:		"this is test comment part1.",
		Tag:		[]string{"tag1", "tag2"},
		Category:	"python",
		CreatedAt:	time.Now(),
	}

	//mock data for db_handler
	postsdto := &infra.PostsDTO{
		Title:		post1.Title,
		Name:		post1.Name,
		Text:		post1.Text,
		Tag:		post1.Tag,
		Category:	post1.Category,
		CreatedAt:	post1.CreatedAt,
	}

	//infra-layer test
	create := infra.DbHandler{}

	err := create.Create(postsdto)  //ここ

	if err != nil {
		fmt.Println(err)
	}

	t := template.Must(template.ParseFiles("templates/base.html", "templates/detail.html", "templates/sidebar.html"))
	t.ExecuteTemplate(writer, "base", post1)
}
