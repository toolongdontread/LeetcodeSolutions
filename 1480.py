class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        aList = []
        for i in range(len(nums)):
            aList.append(sum(nums[:i+1]))
        return aList