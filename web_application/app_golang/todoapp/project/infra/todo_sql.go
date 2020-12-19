package infra

import (
	"time"
)

type TodoModelDTO struct {
	Id		int
	Title	string
	Status	string
	Date	time.Time
}

type TodoInfra interface {
	FindAll() ([]*TodoModelDTO, error)
	//FindByID(int) (*TodoModelDTO, error)
	Insert(*TodoModelDTO) (*TodoModelDTO, error)  //引数でmodel.TodoModelを渡しておくと、DBに保存するときにプロパティの値をそのまま使える
	Update(*TodoModelDTO) (error)
	Delete(*TodoModelDTO) error
	//Putは、DeleteとInsertを組み合わせればいいかな？
}

//下でInsertを実装しているからrepository.TodoRepositoryインタフェースを満たしていることに注意
type todoInfra struct {
	sqlHandler *SqlHandler
}

//コンストラクタ(構造体の初期化)、インスタンスを持ちたいところで呼ぶようにする。つまりmainで呼ぶ。
func NewTodoInfra(sqlHandler *SqlHandler) TodoInfra {
	todoInfra := new(todoInfra)
	todoInfra.sqlHandler = sqlHandler
	return todoInfra  //newによる初期化だから&がついているとみなされる
}

func (ti *todoInfra) Insert(todoModel *TodoModelDTO) (*TodoModelDTO, error) {
	statement := "insert into todos (title, status, date) values ($1, $2, $3) returning id, date"
	stmt, err := ti.sqlHandler.Conn.Prepare(statement)
	if err != nil {
		return todoModel, err
	}
	defer stmt.Close()
	err = stmt.QueryRow(todoModel.Title, todoModel.Status, todoModel.Date).Scan(&todoModel.Id, &todoModel.Date)
	return todoModel, err
}

func (ti *todoInfra) FindAll() (todos []*TodoModelDTO, err error) {
	rows, err := ti.sqlHandler.Conn.Query("SELECT * FROM todos")
	if err != nil {
		return todos, err
	}
	defer rows.Close()
	for rows.Next() {
		todo := &TodoModelDTO{}
		err := rows.Scan(&todo.Id, &todo.Title, &todo.Status, &todo.Date)
		if err != nil {
			return todos, err
		}
		todos = append(todos, todo)
	}
	return
}

func (ti *todoInfra) Update(todoModel *TodoModelDTO) error {
	query := "update todos set title=$1, Status=$2, Date=$3 "
	query += "where id=$4 returning id"
	_, err := ti.sqlHandler.Conn.Exec(query, todoModel.Title, todoModel.Status, todoModel.Date, todoModel.Id)
	return err
}

func (ti *todoInfra) Delete(todoModel *TodoModelDTO) error {
	query := "delete from todos where id=$1"
	_, err := ti.sqlHandler.Conn.Exec(query, todoModel.Id)
	return err
}