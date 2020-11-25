package presentation

import (
	"net/http"
	"errors"
	"techblog/domain"
)

// Checks if the user is logged in and has a session, if not err is not nil
func session(writer http.ResponseWriter, request *http.Request) (sess domain.Session, err error) {
	cookie, err := request.Cookie("_cookie")
	if err == nil {
		sess = domain.Session{Uuid: cookie.Value}
		if ok, _ := sess.Check(); !ok {
			err = errors.New("Invalid session")
		}
	}
	return
}