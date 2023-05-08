class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        aList = []
        bList = []
        count = 0

        for i in range(1, a+1):
            if a%i == 0:
                aList.append(i)
                
        for j in range(1, b+1):
            if b%j == 0:
                bList.append(j)
        
        for k in bList:
            if k in aList:
                count+=1
        

        return count