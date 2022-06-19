package main

func moveZeroes(nums []int) {
	nullPoss := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[i], nums[nullPoss] = nums[nullPoss], nums[i]
			nullPoss++
		}
	}
}

func main() {
	moveZeroes([]int{0, 1, 0, 3, 12})
}
