class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        c=0
        while k>0:
            c+=nums[-1]
            nums[-1] += 1
            k-=1
        return c