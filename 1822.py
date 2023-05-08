class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c = 1
        for i in nums:
            c *= i
        if c > 0:
            return 1
        elif c == 0:
            return 0
        else:
            return -1