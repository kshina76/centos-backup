package domain

import (
	"time"
)

type Post struct {
	Id        int
	Uuid      string
	Name      string
	Title     string
	Body      string
	UserId    string
	CreatedAt time.Time
}

func (user *User) CreatePost(title string, body string) (post Post, err error){
	statement := "insert into posts (uuid, name, title, body, user_id, created_at) values ($1, $2, $3, $4, $5, $6) "
	statement += "returning id, uuid, name, title, body, user_id, created_at"
	stmt, err := Db.Prepare(statement)
	if err != nil {
		return
	}
	defer stmt.Close()
	// use QueryRow to return a row and scan the returned id into the Session struct
	err = stmt.QueryRow(createUUID(), user.Name, title, body, user.Id, time.Now()).Scan(&post.Id, &post.Uuid, &post.Name, &post.Title, &post.Body, &post.UserId, &post.CreatedAt)
	return
}