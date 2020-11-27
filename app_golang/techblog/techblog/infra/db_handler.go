package infra

import (
	"github.com/lib/pq"
	"time"
	//"fmt"
)

//PostsDTO is bridge between usecase and infra layer
type PostsDTO struct {
	Id			int
	Title		string
	Name		string
	Text		string
	Tag			[]string
	Category	string
	CreatedAt	time.Time
}

//DbHandler is used by usecase-layer
type DbHandler interface {
	Create(*PostsDTO) (error)
	FindByID(int) (*PostsDTO, error)
	FindAll() ([]*PostsDTO, error)
	//FindByTag
	//FindByCategory
	//Delete
	//Update
}

//class
type dbHandler struct {}

//NewDbHandler is used by usecase
func NewDbHandler() DbHandler {
	dbHandler := new(dbHandler)
	return dbHandler
}

//Create is used by usecase-layer
func (dh *dbHandler) Create(postsDTO *PostsDTO) (err error) {
	statement := "insert into posts (title, name, text, tag, category, created_at) "
	statement += "values ($1, $2, $3, $4, $5, $6) returning id"
	stmt, err := Db.Prepare(statement)
	defer stmt.Close()
	err = stmt.QueryRow(postsDTO.Title, postsDTO.Name, postsDTO.Text, pq.Array(postsDTO.Tag), postsDTO.Category, postsDTO.CreatedAt).Scan(&postsDTO.Id)
	if err != nil {
		return
	}
	return
}

//FindAll is used by usecase
func (dh *dbHandler) FindAll() (postsDTO []*PostsDTO, err error) {
	query := "select * from posts"
	rows, err := Db.Query(query)
	if err != nil {
		return postsDTO, err
	}
	defer rows.Close()
	for rows.Next() {
		postDTO := &PostsDTO{}
		err := rows.Scan(&postDTO.Id, &postDTO.Title, &postDTO.Name, &postDTO.Text, pq.Array(&postDTO.Tag), &postDTO.Category, &postDTO.CreatedAt)
		if err != nil {
			return postsDTO, err
		}
		postsDTO = append(postsDTO, postDTO)
	}
	return
}

//FindByID is used by usecase
func (dh *dbHandler) FindByID(articleID int) (postDTO *PostsDTO, err error) {
	query := "select * from posts where id = $1"
	postDTO = &PostsDTO{}
	err = Db.QueryRow(query, articleID).Scan(&postDTO.Id, &postDTO.Title, &postDTO.Name, &postDTO.Text, pq.Array(&postDTO.Tag), &postDTO.Category, &postDTO.CreatedAt)
	if err != nil {
		return
	}
	return
}

//Tagモデルを作らないとだめ
//func (dh *dbHandler) FindByTag(articleTag string) (postDTO *PostsDTO, err error) {}
