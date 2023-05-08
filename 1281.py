class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=str(n)
        b=1
        c=0
        for i in a:
            b*=int(i)
            c+=int(i)
        return b-c