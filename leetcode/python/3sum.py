from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = {}
        nums = sorted(nums)
        for fsi in range(len(nums)):
            if fsi > 0 and nums[fsi] == nums[fsi-1]:
                continue

            l, r = fsi+1, len(nums) - 1

            while l < r:
                sum3 = nums[fsi] + nums[l] + nums[r]
                if sum3 == 0:
                    sortSum = sorted([nums[fsi], nums[l], nums[r]])
                    sums["{}_{}-{}".format(sortSum[0], sortSum[1], sortSum[2])] = sortSum
                    l += 1
                elif sum3 > 0:
                    r -= 1
                elif sum3 < 0:
                    l += 1        

        return [sums[i] for i in sums]
        
sol = Solution()
print(sol.threeSum([-3, 3, 4, -3, 1, 2]))
print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([0,1,1]))   
print(sol.threeSum([0,0,0]))   