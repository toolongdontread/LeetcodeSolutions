class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        aList = s.split(" ")
        return len(aList[-1])