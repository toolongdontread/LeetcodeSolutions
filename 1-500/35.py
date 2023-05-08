class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a = nums.count(target)
        if a != 0:
            return nums.index(target)
        else:
            for i in nums:
                if i >= target:
                    return nums.index(i)
                    break
        return len(nums)