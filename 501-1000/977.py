class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        aList = [x**2 for x in nums]
        aList.sort()
        return aList