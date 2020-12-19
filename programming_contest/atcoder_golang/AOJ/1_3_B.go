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
	//sc.Split(bufio.ScanWords) スペース区切りの時に使う

	N := 10000
	for i := 0; i < N; i++ {
		fmt.Printf("Case %d: %s\n", i+1, nextLine())
	}
}
