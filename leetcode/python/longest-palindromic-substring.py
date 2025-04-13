class Solution:
    def longestPalindrome(self, s: str) -> str:
       if len(s) < 2:
           return s
       max_pal = ''
       for i in range(len(s)-1):
           j = i + 1
           while j <= len(s):
               orig = s[i:j]
               invert = orig[::-1]
               print(orig, invert)
               if orig == invert and len(orig) > len(max_pal):
                   max_pal = orig
               j += 1
       return max_pal     

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome("bb"))  
    #print(sol.longestPalindrome("babad")) 
    #print(sol.longestPalindrome("cbbd"))  
