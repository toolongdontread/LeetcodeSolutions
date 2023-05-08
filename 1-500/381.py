class RandomizedCollection:

    def __init__(self):
        self.aList = []

    def insert(self, val: int) -> bool:
        if self.aList.count(val) == 0:
            self.aList.append(val)
            return True
        self.aList.append(val)
        return False

    def remove(self, val: int) -> bool:
        if val in self.aList:
            self.aList.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return self.aList[random.randint(0, len(self.aList)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()