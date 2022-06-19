package main

import (
	"fmt"
	"math"
)

func convert(s string, numRows int) string {
	var zigzagString string
	rows := int(math.Min(float64(numRows), float64(len(s))))

	zigzag := make([]string, rows)
	for i := 0; i < rows; i++ {
		zigzag[i] = ""
	}
	yDir := 0
	y := 0

	for i := 0; i < len(s); i++ {

		if int(y) >= int(rows) {
			break
		}

		zigzag[y] += string(s[i])

		if y == rows-1 && rows != 1 {
			yDir = -1
		}

		if y == 0 && rows != 1 {
			yDir = 1
		}

		y += yDir
	}

	for y = 0; y < len(zigzag); y++ {
		zigzagString += zigzag[y]
	}

	return zigzagString
}

func main() {
	fmt.Println(convert("PAYPALISHIRING", 3))
	fmt.Println(convert("PAYPALISHIRING", 4))
	fmt.Println(convert("AB", 1))
	fmt.Println(convert("A", 1))
}
