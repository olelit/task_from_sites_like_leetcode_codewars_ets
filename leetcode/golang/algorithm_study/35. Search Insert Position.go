package main

import "fmt"

func searchInsert(nums []int, target int) int {
	if target > nums[len(nums)-1] {
		return len(nums)
	}

	if target < nums[0] {
		return 0
	}

	left := 0
	right := len(nums) - 1

	for left < right-1 {
		middle := (left + right) / 2

		if nums[middle] == target {
			return middle
		}

		if nums[middle] > target {
			right = middle
		}
		if nums[middle] < target {
			left = middle
		}
	}

	if nums[left] < target {
		return left + 1
	}

	if nums[left] == target {
		return left
	}

	return right + 1
}

func main() {
	fmt.Println(searchInsert([]int{1, 3, 5}, 4))
	fmt.Println(searchInsert([]int{1, 3}, 3))
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 5))
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 2))
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 7))
}
