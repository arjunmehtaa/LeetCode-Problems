class RandomizedSet:

    def __init__(self):
        self.dataSet = {}
        self.dataList = []
        
    def insert(self, val: int) -> bool:
        if val in self.dataSet:
            return False
        self.dataSet[val] = len(self.dataList) 
        self.dataList.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.dataSet:
            lastVal = self.dataList[-1]
            self.dataList[self.dataSet[val]] = lastVal
            self.dataList.pop()
            self.dataSet[lastVal] = self.dataSet[val]
            del self.dataSet[val]
            return True
        return False
        
    def getRandom(self) -> int:
        return random.choice(self.dataList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()