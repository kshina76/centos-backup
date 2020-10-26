package main

import (
	"fmt"
)

type Printer interface {
	PrintVal()
	PrintStr()
}

type Literal struct {
	val int
	str string
}

func (l *Literal) PrintVal() {
	fmt.Println(l.val)
}

func (l *Literal) PrintStr() {
	fmt.Println(l.str)
}

func main() {
	//Printer型(interface型)の変数を定義
	var p Printer

	l := Literal{3, "hello"}
	l.PrintVal()

	//PrintStrとPrintValの両方を実装していないとエラーになる
	p = &l


}