package main

import (
	"net/http"
	//"html/template"
	"techblog/presentation"
	"techblog/infra"
	"techblog/usecase"
	"github.com/gorilla/mux"
)

func main() {
	//DI
	dh := infra.NewDbHandler()
	tbu := usecase.NewTechblogUsecase(dh)
	tp := presentation.NewTechblogPresentation(tbu)

	r := mux.NewRouter()
	//r := http.NewServeMux()

	//静的ファイルの設定
	files := http.FileServer(http.Dir("./static/"))
	r.PathPrefix("/static/").Handler(http.StripPrefix("/static/", files))
	//r.Handle("/static/", http.StripPrefix("/static/", files))

	//トップページ
	r.HandleFunc("/", tp.ListPosts)

	//詳細ページ
	r.HandleFunc("/detail/{id:[0-9]+}", tp.DetailPost)

	//記事作成
	r.HandleFunc("/create", tp.CreatePosts)

	//アカウント作成
	mux.HandleFunc("/signup", presentation.signUp)
	//mux.HandleFunc("/signup-account", presentation.SignupAccount)

	//ログイン
	//mux.HandleFunc("/login", presentation.Login)
	//mux.HandleFunc("/authenticate", presentation.Authenticate)

	//mux.HandleFunc("/admin", presentation.Admin)
	//mux.HandleFunc("/post-article", presentation.PostArticle)

	//サーバ起動
	server := &http.Server {
		Addr: "0.0.0.0:8080",
		Handler: r,
	}
	server.ListenAndServe()
}
