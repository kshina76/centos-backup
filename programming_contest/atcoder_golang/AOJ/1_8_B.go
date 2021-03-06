package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	"regexp"
	"strings"
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

//(正規表現, 判定したい文字列)
func check_regexp(reg, str string) bool {
  return regexp.MustCompile(reg).Match([]byte(str))
}

func main() {
	//sc.Split(bufio.ScanWords) //スペース区切りの時に使う

}
