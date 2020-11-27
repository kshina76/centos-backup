package infra

import (
	//"github.com/lib/pq"
	"time"
	"fmt"
)

//PostsDTO is bridge between usecase and infra layer
type PostsDTO struct {
	Title		string
	Name		string
	Text		string
	Tag			[]string
	Category	string
	CreatedAt	time.Time
}

//DbHandler is used by usecase-layer
//type DbHandler interface {
//	Create(PostsDTO) (int, error)
	//Find
	//FindAll
	//Delete
	//Update
//}

//DbHandler is used by test あとで小文字に直す
type DbHandler struct {}

//Create is used by test DbHandlerをあとで小文字に直す
func (dh *DbHandler) Create(postsDTO *PostsDTO) (err error) {
	statement := "insert into Posts (title, name, text, category, createdAt) "
	statement += "values ($1, $2, $3, $4, $5) returning id"
	stmt, err := Db.Prepare(statement)
	fmt.Println(postsDTO)
	defer stmt.Close()
	var idd int
	err = stmt.QueryRow(postsDTO.Title, postsDTO.Name, postsDTO.Text, postsDTO.Category, postsDTO.CreatedAt).Scan(&idd)  //ここでエラー
	//, pq.Array(postsDTO.Tag)
	if err != nil {
		return
	}
	return
}
