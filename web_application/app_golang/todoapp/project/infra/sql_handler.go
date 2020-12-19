package infra

import (
	"database/sql"
	"log"
	_ "github.com/lib/pq"
)

type SqlHandler struct {
	Conn *sql.DB
}

//コンストラクタ(構造体の初期化)
func NewSqlHandler() *SqlHandler {
	Conn, err := sql.Open("postgres", "host=postgres user=app_user dbname=app_db password=password sslmode=disable")
	if err != nil {
		log.Fatal(err)
	}
	sqlHandler := new(SqlHandler)
	sqlHandler.Conn = Conn
	return sqlHandler
}