class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        aList = []
        for i in range(len(nums)):
            aList.insert(index[i], nums[i])
        return aList