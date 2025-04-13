package main

import "fmt"

func mostPoints(questions [][]int) int64 {
	var solve func(i int) int
	n := len(questions)
	cache := make([]int, n)

	for i := range cache {
		cache[i] = 0
	}

	solve = func(i int) int {
		if i >= n {
			return 0
		}

		if cache[i] != 0 {
			return cache[i]
		}

		take := questions[i][0] + solve(i+questions[i][1]+1)
		skip := solve(i + 1)

		cache[i] = max(take, skip)
		return cache[i]
	}

	return int64(solve(0))
}

func main() {
	fmt.Println(mostPoints([][]int{{21, 5}, {92, 3}, {74, 2}, {39, 4}, {58, 2}, {5, 5}, {49, 4}, {65, 3}}))
}
