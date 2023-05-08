class Solution:
    def arrangeCoins(self, n: int) -> int:
        m=1
        c=0
        for i in range(n):
            if n - m >= 0:
                n=n-m
            else:
                break
            c+=1
            m+=1
        return c