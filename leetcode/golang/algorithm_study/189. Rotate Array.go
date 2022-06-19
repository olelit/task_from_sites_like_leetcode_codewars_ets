package main

import "fmt"

func rotate(nums []int, k int) []int {
	l := len(nums)
	if k > l {
		k %= l
	}
	if k == 0 {
		return []int{}
	}
	rotated := make([]int, len(nums))
	for i := 0; i < l; i++ {
		if i < k {
			rotated[i] = nums[(l-k)+i]
		} else {
			rotated[i] = nums[i-k]
		}
	}
	return rotated
}

func main() {
	fmt.Println(rotate([]int{-1}, 2))
	fmt.Println(rotate([]int{1, 2, 3, 4, 5, 6, 7}, 3))
	fmt.Println(rotate([]int{-1, -100, 3, 99}, 2))
}
