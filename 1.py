class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aList = []
        
        for i in nums:
            for j in range(1,len(nums)):
                if i+nums[j] == target and nums.index(i) != j:
                    aList.append(nums.index(i))
                    aList.append(j)
                    break
            if len(aList) == 2:
                break
        return aList