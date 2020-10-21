package main

import (
	"fmt"
	"net/http"
)

func handler(writer http.ResponseWriter, request *http.Request) {
	fmt.Fprintf(writer, "Hello world, %s", request.URL.Path[1:])
}

func main() {
	//djangoでいうURLディスパッチャみたいなもの。
	//http://localhost:8080/にアクセスがあったら、handlerという名前の関数のハンドラに処理をさせる(リダイレクト)という意味
	http.HandleFunc("/", handler)
	
	//第一引数にListenするポートを指定、第二引数にハンドラを指定(nilにするとデフォルトのDefaultServeMuxが使われる)
	http.ListenAndServe(":8080", nil)
}