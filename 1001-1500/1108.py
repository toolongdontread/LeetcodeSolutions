class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = address.count(".")
        address = address.replace(".","[.]", a)
        return address