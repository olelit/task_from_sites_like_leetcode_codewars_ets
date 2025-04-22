from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
    
        prefix = strs[0]

        for i in range(1, len(strs)):
            temp = ''
            cur = strs[i]
            ci = pi = 0
            while ci < len(cur) and pi < len(prefix) and cur[ci] == prefix[ci]:
                    temp += cur[ci]
                    ci+=1
                    pi+=1

            if temp == '':
                return ''
            prefix = temp
            
        return prefix
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(["cir","car"]))
    print(sol.longestCommonPrefix(["ab", "a"]))
    print(sol.longestCommonPrefix(["flower","flow","flight"]))
    print(sol.longestCommonPrefix(["dog","racecar","car"]))