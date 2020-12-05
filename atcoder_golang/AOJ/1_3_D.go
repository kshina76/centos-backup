// +build ignore

package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	//"strings"
)
var sc = bufio.NewScanner(os.Stdin)

//スペース区切りで読み込む
func nextInt() int {
	sc.Scan()
	i, err := strconv.Atoi(sc.Text())
	if err != nil {
		panic(err)
	}
	return i
}

//一行毎に読み込む
func nextLine() string {
	sc.Scan()
	return sc.Text()
}

func main() {
	sc.Split(bufio.ScanWords) //スペース区切りの時に使う
	a := nextInt()
	b := nextInt()
	c := nextInt()

	var n int
	if b <= c {
		n = b
	}else {
		n = c
	}

	remain := 0
	for i := a; i <= n; i++ {
		if c % i == 0 {
			remain++
		}
	}
	fmt.Println(remain)
}
