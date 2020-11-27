package infra

import (
	//PostgreSQL Driver
	_ "github.com/lib/pq"
	"database/sql"
	"log"
)

//Db is used by db_handler.go
var Db *sql.DB

func init() {
	var err error
	Db, err = sql.Open("postgres", "host=postgres user=app_user db_name=app_db password=password sslmode=disable")
	if err != nil {
		log.Fatal(err)
	}
	return
}
