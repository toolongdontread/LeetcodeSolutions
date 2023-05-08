class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        aList = []
        for i in range(len(nums)):
            aList.append(nums[nums[i]])
        return aList