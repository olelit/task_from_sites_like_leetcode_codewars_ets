package main

import (
	"fmt"
)

func searchB(nums []int, target int, pos int) int {

	right := len(nums) - 1
	middle := right / 2

	if right < 0 || (right == 0 && nums[0] != target) {
		return -1
	} else if nums[middle] == target {
		if pos > middle {
			return pos + middle
		}
		return middle
	} else if nums[middle] > target {
		return searchB(nums[:middle], target, pos)
	} else if nums[middle] < target {
		pos += middle + 1
		return searchB(nums[middle+1:], target, pos)
	}

	return pos
}

func search(nums []int, target int) int {

	if len(nums) == 1 && nums[0] == target {
		return 0
	}

	if len(nums) == 1 && nums[0] != target {
		return -1
	}

	return searchB(nums, target, 0)
}

func main() {
	fmt.Println(search([]int{2, 5}, 0))
	fmt.Println(search([]int{5}, 5))
	fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 9))
	fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 12))
	fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 2))
	fmt.Println(search([]int{2, 5}, 5))
	fmt.Println(search([]int{2, 5}, 2))
}
