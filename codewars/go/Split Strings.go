package main

import "fmt"

func Solution(str string) []string {
	var split []string
	var pair string
	for i := 0; i < len(str); i++ {
		pair += string(str[i])
		if len(pair) == 2 {
			split = append(split, pair)
			pair = ""
		}
	}

	if len(pair) == 1 {
		pair += "_"
		split = append(split, pair)
	}

	return split
}

func main() {
	fmt.Println(Solution("abc"))
	fmt.Println(Solution("abcdef"))
}
