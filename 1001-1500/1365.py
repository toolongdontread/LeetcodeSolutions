class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        aList = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            aList.append(count)
            count = 0
        return aList