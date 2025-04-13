from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combList = []

        def recurs(l: int, r: int, parenthesis: List[str]) -> List[str]:
            if l == 0 and r == 0:
                combList.append("".join(parenthesis))
                return

            if l > 0:
                parenthesis.append('(')
                recurs(l - 1, r, parenthesis)
                parenthesis.pop()
            
            if r > l:
                parenthesis.append(')')
                recurs(l, r - 1, parenthesis)
                parenthesis.pop()   
    
        
        recurs(n, n, [])
        return combList

if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(3))
    #print(sol.generateParenthesis(1))