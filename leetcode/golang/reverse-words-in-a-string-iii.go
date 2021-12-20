package main

import (
	"fmt"
)

func reverseWords(s string) string {
	var words []string
	from := 0
	for i := 0; i < len(s); i++ {
		if s[i] == ' ' {
			words = append(words, s[from:i])
			from = i + 1
		} else if i == len(s)-1 {
			words = append(words, s[from:i+1])
		}
	}
	ans := ""
	for i := 0; i < len(words); i++ {
		ans += reverse(words[i]) + " "
	}
	return ans[:len(ans)-1]
}

func reverse(s string) string {
	revStr := ""
	for i := len(s) - 1; i >= 0; i-- {
		revStr = revStr + string(s[i])
	}

	return revStr
}

func main() {
	fmt.Println(reverseWords("Let's take LeetCode contest"))
	fmt.Println(reverseWords("God Ding"))
}
