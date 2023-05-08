class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s2=""
        for i in range(len(indices)):
            s2+=s[indices.index(i)]
        return s2