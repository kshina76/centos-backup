package presentation

import(
	"net/http"
	"html/template"
	"time"
	//test
	//"techblog/infra"
	"techblog/usecase"
	"github.com/gorilla/mux"
	"fmt"
	"strconv"
)

//Posts struct is exposed, this is mock data
type Posts struct {
	Id			int
	Title		string
	Name		string
	Text		string
	Tag			[]string
	Category	string
	CreatedAt	time.Time
}

//TechblogPresentation is used by main
type TechblogPresentation interface {
	ListPosts(http.ResponseWriter, *http.Request)
	DetailPost(http.ResponseWriter, *http.Request)
	CreatePosts(http.ResponseWriter, *http.Request)
}

type techblogPresentation struct {
	techblogUsecase usecase.TechblogUsecase
}

//NewTechblogPresentation is used by constracta
func NewTechblogPresentation(techblogUsecase usecase.TechblogUsecase) TechblogPresentation{
	techblogPresentation := new(techblogPresentation)
	techblogPresentation.techblogUsecase = techblogUsecase
	return techblogPresentation
}

//ListPosts function is exposed
func (tbp *techblogPresentation) ListPosts(writer http.ResponseWriter, request *http.Request) {
	posts, err := tbp.techblogUsecase.DisplayPosts()
	if err != nil {
		fmt.Println(err)
	}
	t := template.Must(template.ParseFiles("templates/base.html", "templates/article.html", "templates/sidebar.html"))
	t.ExecuteTemplate(writer, "base", posts)
}

//DetailPost function is exposed
func (tbp *techblogPresentation) DetailPost(writer http.ResponseWriter, request *http.Request) {
	vars := mux.Vars(request)
	err := request.ParseForm()
	if err != nil {
		fmt.Println("cannot parse form")
	}
	articleID, _ := strconv.Atoi(vars["id"])
	post, err := tbp.techblogUsecase.DisplayDetailPosts(articleID)
	t := template.Must(template.ParseFiles("templates/base.html", "templates/detail.html", "templates/sidebar.html"))
	t.ExecuteTemplate(writer, "base", post)
}

//CreatePosts is used by main.go
func (tbp *techblogPresentation) CreatePosts(writer http.ResponseWriter, request *http.Request) {
	post1 := &usecase.Posts {
		Title:		"mock title1",
		Name:		"Kosuke",
		Text:		"this is test comment part1.",
		Tag:		[]string{"tag1", "tag2"},
		Category:	"python",
		CreatedAt:	time.Now(),
	}
	err := tbp.techblogUsecase.CreatePosts(post1)
	if err != nil {
		fmt.Println(err)
	}
}
