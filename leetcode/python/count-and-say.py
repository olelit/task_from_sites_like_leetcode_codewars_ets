class Solution:
    def countAndSay(self, n: int) -> str:
        rle = '1'  

        for j in range (1, n):
            rle = self.caclRle(rle)
        return rle
    
    def caclRle(self, rle: str) -> str:
            rleL = list(rle)
            tempRle = ''
            c = 1
            for i in range(len(rleL)):
                if i < len(rleL) - 1 and rleL[i] == rleL[i + 1]:
                    c +=1
                else:
                    tempRle += str(c) + rle[i]
                    c = 1   
            return tempRle
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.countAndSay(6)) 
    print(sol.countAndSay(4))    
    print(sol.countAndSay(1))       