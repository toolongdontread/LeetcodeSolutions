class RandomizedSet:

    def __init__(self):
        self.aList = []

    def insert(self, val: int) -> bool:
        if val not in self.aList:
            self.aList.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.aList:
            self.aList.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        self.r = random.randint(0,len(self.aList)-1)
        return self.aList[self.r]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()