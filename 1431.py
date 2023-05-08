class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        aList = []
        for i in candies:
            if i + extraCandies >= max(candies):
                aList.append(True)
            else:
                aList.append(False)
        return aList