def get_count_iteration(nums,  count_iteration):

    if len(nums) == 0:
        return 0

    nums.sort()
    for i in range(len(nums)):
        if i == 0:
            continue

        if nums[i] == nums[i - 1]:
            nums[i] += 1
            count_iteration += 1

            return get_count_iteration(nums, count_iteration)
    return count_iteration


if __name__ == '__main__':
    print(get_count_iteration([1, 2, 2], 0))
    print(get_count_iteration([3, 2, 1, 2, 1, 7], 0))
