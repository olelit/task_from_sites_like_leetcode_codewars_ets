package main

import (
	"fmt"
	"strings"
)

func High(s string) string {
	split := strings.Split(s, " ")
	max := split[0]

	for i := 1; i < len(split); i++ {
		if letterSum(split[i]) > letterSum(max) {
			max = split[i]
		}
	}

	return max
}

func alphaNum(letter rune) int {
	char := int(letter)
	char -= 96
	return char
}

func letterSum(str string) int {
	sum := 0
	for i := 0; i < len(str); i++ {
		sum += alphaNum(rune(str[i]))
	}
	return sum
}

func main() {
	fmt.Println(alphaNum('a'))
	fmt.Println(High("man i need a taxi up to ubud"))
	fmt.Println(High("what time are we climbing up the volcano"))
	fmt.Println(High("take me to semynak"))
}
