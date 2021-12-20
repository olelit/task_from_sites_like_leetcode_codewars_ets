package main

import "fmt"

func numJewelsInStones(jewels string, stones string) int {
	jewelCount := 0

	for _, letter := range jewels {
		for _, stoneLetter := range stones {
			if letter == stoneLetter {
				jewelCount++
			}
		}
	}

	return jewelCount
}

func main() {
	fmt.Println(numJewelsInStones("aA", "aAAbbbb"))
	fmt.Println(numJewelsInStones("z", "ZZ"))
}
