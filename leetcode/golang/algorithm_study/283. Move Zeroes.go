package main

func moveZeroes(nums []int) {
	lastZeroIndex := -1

	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 && lastZeroIndex == -1 {
			lastZeroIndex = i
		}

		if nums[i] != 0 && lastZeroIndex != -1 {
			nums[lastZeroIndex] = nums[i]
			nums[i] = 0
			lastZeroIndex += 1
		}
	}
}

func main() {
	moveZeroes([]int{0, 1, 0, 3, 12})
	moveZeroes([]int{0})
}
