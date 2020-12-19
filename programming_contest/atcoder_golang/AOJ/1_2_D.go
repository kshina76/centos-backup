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

func nextInt() int {
	sc.Scan()
	i, err := strconv.Atoi(sc.Text())
	if err != nil {
		panic(err)
	}
	return i
}

/*
package D_1_2 -> mainにして実行する
D_1_2 -> mainにして実行する

エッジパターン(境界の部分)の数値を調べて、図に書いて、条件式を書いていくと
x>=r && y>=r ... 1
x+r <= W ... 2
y+r<=H ... 3
という条件が出てくる
*/
func main() {
	sc.Split(bufio.ScanWords)
	W := nextInt()
	H := nextInt()
	x := nextInt()
	y := nextInt()
	r := nextInt()

	if (x < r || y < r) {
		fmt.Println("No")
	}else if x + r > W || y + r > H {
		fmt.Println("No")
	}else{
		fmt.Println("Yes")
	}

}
