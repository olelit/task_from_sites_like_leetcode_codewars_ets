from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return -1

        sortedSet = sorted(set(nums))
        ln = len(sortedSet)
        frEl = sortedSet[0]
        if frEl < k:
            return -1
        
        return ln - 1 if frEl == k else ln
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperations([5,2,5,4,5], 2))
    print(sol.minOperations([2,1,2], 2))
    print(sol.minOperations([9,7,5,3], 1))
        