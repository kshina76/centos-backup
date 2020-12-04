package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	//"strings"
)
var sc = bufio.NewScanner(os.Stdin)

//スペース区切りでint型で読み込む
func nextInt() int {
	sc.Scan()
	i, err := strconv.Atoi(sc.Text())
	if err != nil {
		panic(err)
	}
	return i
}

//スペース区切りでfloat型で読み込む
func nextFloat64() float64 {
	sc.Scan()
	f, err := strconv.ParseFloat(sc.Text(), 64)
	if err != nil {
		panic(err)
	}
	return f
}

//一行毎に読み込む
func nextLine() string {
	sc.Scan()
	return sc.Text()
}

func main() {
	sc.Split(bufio.ScanWords) //スペース区切りの時に使う


}
