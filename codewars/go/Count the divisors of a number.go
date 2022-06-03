package main

import "fmt"

func Divisors(n int) int {
	count := 0
	for i := 1; i <= n/2; i++ {
		if n%i == 0 {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(Divisors(1))
	fmt.Println(Divisors(10))
	fmt.Println(Divisors(11))
	fmt.Println(Divisors(54))
	fmt.Println(Divisors(64))
	fmt.Println(Divisors(500000))
}
