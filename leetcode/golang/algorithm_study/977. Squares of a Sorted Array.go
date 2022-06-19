package main

import "fmt"

func sortedSquares(nums []int) []int {
	left := 0
	right := len(nums) - 1
	sortedSqr := make([]int, len(nums))

	for i := len(nums) - 1; i >= 0; i-- {
		if sqr(nums[left]) > sqr(nums[right]) {
			sortedSqr[i] = sqr(nums[left])
			left++
		} else {
			sortedSqr[i] = sqr(nums[right])
			right--
		}
	}

	return sortedSqr
}

func sqr(num int) int {
	return num * num
}

func main() {
	//fmt.Println(sortedSquares([]int{-4, -1, 0, 3, 10}))
	fmt.Println(sortedSquares([]int{-7, -3, 2, 3, 11}))
}
