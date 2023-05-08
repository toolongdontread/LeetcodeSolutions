class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for j in digits:
            s+=str(j)
        a=int(s)+1
        s2=str(a)
        aList = []
        for i in s2:
            aList.append(int(i))
        return aList