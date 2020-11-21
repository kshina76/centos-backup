package infra

import (
	//これを使ってしまうとusecaseとinfraが相互参照してしまっているからレイヤードに置いてダメかも
	//DTOという手法を適用すると解決できるらしい
	//https://qiita.com/tono-maron/items/345c433b86f74d314c8d#純粋なレイヤードアーキテクチャの場合
	//"project/usecase"

)

type TodoModelDTO struct {
	Id		int
	Title	string
	Status	string
	Date	time.Time
}

type TodoSqlAction interface {
	//FindAll()
	//Find
	Insert(todo *usecase.TodoModel) (*usecase.TodoModel, error)  //引数でmodel.TodoModelを渡しておくと、DBに保存するときにプロパティの値をそのまま使える
	//Delete()
	//Putは、DeleteとInsertを組み合わせればいいかな？
}

//下でInsertを実装しているからrepository.TodoRepositoryインタフェースを満たしていることに注意
type TodoInfra struct {
	sqlHandler SqlHandler
}

//コンストラクタ(構造体の初期化)、インスタンスを持ちたいところで呼ぶようにする。つまりmainで呼ぶ。
func NewTodoInfra(sqlHandler SqlHandler) TodoSqlAction {
	todoInfra := new(TodoInfra)
	todoInfra.sqlHandler = sqlHandler
	return todoInfra  //newによる初期化だから&がついているとみなされる
}

//メソッド
func (todoInfra *TodoInfra) Insert(todoModel *usecase.TodoModel) (*usecase.TodoModel, error){
	statement := "insert into users (title, status, date) values ($1, $2, $3) returning id, date"
	stmt, err := todoInfra.sqlHandler.Conn.Prepare(statement)
	if err != nil {
		return
	}
	defer stmt.Close()
	err = stmt.QueryRow(todoModel.Title, todoModel.Status, todoModel.Date).Scan(&todoModel.Id, &todoModel.Date)
	return todoModel, err
}