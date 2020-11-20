package infra

import (
	"project/domain/repository"
	"project/model"
)

//下でInsertを実装しているからrepository.TodoRepositoryインタフェースを満たしていることに注意
type TodoRepository struct {
	sqlHandler SqlHandler
}

//コンストラクタ(構造体の初期化)、インスタンスを持ちたいところで呼ぶようにする。つまりmainで呼ぶ。
func NewTodoRepository(sqlHandler SqlHandler) repository.TodoRepository {
	todoRepository := new(TodoRepository)
	todoRepository.sqlHandler = sqlHandler
	return todoRepository  //newによる初期化だから&がついているとみなされる
}

//メソッド
func (todoRepo *TodoRepository) Insert(todoModel *model.TodoModel) (*model.TodoModel, error){
	statement := "insert into users (title, status, date) values ($1, $2, $3) returning id, date"
	stmt, err := todoRepo.sqlHandler.Conn.Prepare(statement)
	if err != nil {
		return
	}
	defer stmt.Close()
	err = stmt.QueryRow(todoModel.Title, todoModel.Status, todoModel.Date).Scan(&todoModel.Id, &todoModel.Date)
	return todoModel, err
}