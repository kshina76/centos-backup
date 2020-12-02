package usecase

import (
	"techblog/infra"
	"time"
	"fmt"
)

type Posts struct {
	Id			int
	Title		string
	Name		string
	Text		string
	Tag			[]string
	Category	string
	CreatedAt	time.Time
}

//TechblogUsecase is used by presentation
type TechblogUsecase interface {
	CreatePosts(*Posts) (error)
	DisplayPosts() ([]*Posts, error)
	DisplayDetailPosts(int) (*Posts, error)
}

type techblogUsecase struct {
	dbHandler infra.DbHandler
}

//NewTechblogUsecase is used by presentation
func NewTechblogUsecase(dbHandler infra.DbHandler) TechblogUsecase{
	techblogUsecase := new(techblogUsecase)
	techblogUsecase.dbHandler = dbHandler
	return techblogUsecase
}

func (tbu *techblogUsecase) CreatePosts(posts *Posts) (err error){
	postsDTO := &infra.PostsDTO{
		Title:		posts.Title,
		Name:		posts.Name,
		Text:		posts.Text,
		Tag:		posts.Tag,
		Category:	posts.Category,
		CreatedAt:	posts.CreatedAt,
	}
	err = tbu.dbHandler.Create(postsDTO)
	if err != nil {
		return
	}
	return
}

func (tbu *techblogUsecase) DisplayPosts() (posts []*Posts, err error) {
	postsDTO, err := tbu.dbHandler.FindAll()
	if err != nil {
		return
	}
	for _, p := range postsDTO {
		post := &Posts{
			Id:			p.Id,
			Title:		p.Title,
			Name:		p.Name,
			Text:		p.Text,
			Tag:		p.Tag,
			Category:	p.Category,
			CreatedAt:	p.CreatedAt,
		}
		posts = append(posts, post)
	}
	return
}

//DisplayDetailPosts is used by presentation
func (tbu *techblogUsecase) DisplayDetailPosts(articleID int) (posts *Posts, err error) {
	postDTO, err := tbu.dbHandler.FindByID(articleID)
	if err != nil {
		return
	}
	posts = &Posts{
		Title:		postDTO.Title,
		Name:		postDTO.Name,
		Text:		postDTO.Text,
		Tag:		postDTO.Tag,
		Category:	postDTO.Category,
		CreatedAt:	postDTO.CreatedAt,
	}
	return
}
