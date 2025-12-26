from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple_sum = sum(apple)
        reversed_capacity = sorted(capacity, reverse=True)

        if reversed_capacity[0] >= apple_sum:
            return 1

        while len(reversed_capacity) > 1:
            sum_capacity = sum(reversed_capacity)
            apple_with_last_cap = apple_sum + reversed_capacity[-1]
            if apple_with_last_cap <= sum_capacity:
                reversed_capacity.pop()
            else:
                break

        return len(reversed_capacity)


if __name__ == '__main__':
    solution = Solution()
    appleArr = [5,5,5]
    capacityArr = [2,4,2,7]
    print(solution.minimumBoxes(appleArr, capacityArr))
