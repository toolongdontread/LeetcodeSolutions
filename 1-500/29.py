class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = dividend/divisor
        if a<-2**31:
            return -2**31
        elif a>2**31-1:
            return 2**31-1
        elif a>0:
            return floor(a)
        else:
            return math.ceil(a)