class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = max(nums)
        for i in range(a):
            if nums.count(i) == 0:
                return i
                break
        return a+1