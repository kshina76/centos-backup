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

//一行毎に読み込む
func nextLine() string {
	sc.Scan()
	return sc.Text()
}

func main() {
	var cols []string
	var a, b int
	for ;; {
		cols = strings.Split(nextLine(), " ")
		a, _ = strconv.Atoi(cols[0])
		b, _ = strconv.Atoi(cols[1])
		if a == 0 && b == 0 {
			break
		}else if a < b {
			fmt.Printf("%d %d\n", a, b)
		}else if a > b {
			fmt.Printf("%d %d\n", b, a)
		}else{
			fmt.Printf("%d %d\n", a, b)
		}
	}
}
