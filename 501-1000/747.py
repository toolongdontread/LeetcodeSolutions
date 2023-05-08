class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        big = max(nums)
        position = nums.index(big)

        nums.sort()

        if big >= nums[-2]*2:
            return position
        return -1