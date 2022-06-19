package main

import "fmt"

func singleNonDuplicate(nums []int) int {
	low := 0
	high := len(nums) - 1

	if high == 0 {
		return nums[0]
	}
	if nums[high] != nums[high-1] {
		return nums[high]
	}
	if nums[low] != nums[low+1] {
		return nums[low]
	}

	for low <= high {
		medium := (low + high) / 2
		mediumEl := nums[medium]
		leftEl := nums[medium-1]
		rightEl := nums[medium+1]

		if mediumEl != leftEl && mediumEl != rightEl {
			return mediumEl
		}

		if ((medium%2) == 0 && mediumEl == rightEl) || ((medium%2) == 1 && mediumEl == leftEl) {
			low = medium + 1
		} else {
			high = medium - 1
		}
	}

	return -1
}

func main() {
	//log 9 = 3
	nums := []int{1, 1, 2, 3, 3, 4, 4, 8, 8}
	fmt.Println(singleNonDuplicate(nums))
	//log 7 = 2.8
	nums = []int{3, 3, 7, 7, 10, 11, 11}
	fmt.Println(singleNonDuplicate(nums))
}
