from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original = [0]
        for i in range(0, len(derived)):
            original.append(original[i] ^ derived[i])

        is_zero_valid = original[0] == original[-1]    

        original = [1]
        for i in range(0, len(derived)):
            original.append(original[i] ^ derived[i])

        is_one_valid = original[0] == original[-1]      

        return is_zero_valid or is_one_valid


sol = Solution()
print(sol.doesValidArrayExist([1,1,0]))
print(sol.doesValidArrayExist([1,1]))
print(sol.doesValidArrayExist([1,0]))