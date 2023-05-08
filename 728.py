class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        a = []
        for i in range(left, right+1):
            c = 0
            s = str(i)
            for j in s:
                if j=="0":
                    break
                if i%int(j) == 0:
                    c+=1

            if(c==len(s)):
                a.append(i)
        return a