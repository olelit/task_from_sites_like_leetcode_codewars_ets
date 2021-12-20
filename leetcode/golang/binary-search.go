package main

import "fmt"

func search(nums []int, target int) int {
	left := 0
	right := len(nums)

	for left < right {
		medium := (left + right) / 2
		if right-left == 1 && target != nums[medium] {
			return -1
		} else if target == nums[medium] {
			return medium
		} else if target > nums[medium] {
			left = medium + 1
		} else {
			right = medium
		}
	}

	return -1
}

func main() {
	fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 9))
	fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 2))
}
