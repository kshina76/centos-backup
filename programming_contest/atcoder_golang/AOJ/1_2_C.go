// +build ignore

package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func nextInt() int {
	sc.Scan()
	i, err := strconv.Atoi(sc.Text())
	if err != nil {
		panic(err)
	}
	return i
}

func main() {
	sc.Split(bufio.ScanWords)

	var val []int
	var strval []string

	//標準出力をスライスに読み込む
	N := 3
	for i := 0; i < N; i++ {
		val = append(val, nextInt())
	}

	//バブルソート
	var tmp int
	for i := 0; i < N-1; i++ {
		for j := i + 1; j < N; j++ {
			if val[i] > val[j] {
				tmp = val[i]
				val[i] = val[j]
				val[j] = tmp
			}
		}
	}

	//int型スライスを文字列型のスライスに変換
	for _, v := range val {
		strval = append(strval, strconv.Itoa(v))
	}

	//文字列型のスライスを空白区切りで出力
	fmt.Println(strings.Join(strval, " "))
}
