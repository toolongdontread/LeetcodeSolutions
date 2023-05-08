class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        aList = []
        for i in range(0, len(nums)-n):
            aList.append(nums[i])
            aList.append(nums[i+n])
        return aList