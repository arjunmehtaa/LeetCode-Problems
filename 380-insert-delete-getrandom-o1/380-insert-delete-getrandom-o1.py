class RandomizedSet:

    def __init__(self):
        self.dataSet = set()
        
    def insert(self, val: int) -> bool:
        if val in self.dataSet:
            return False
        self.dataSet.add(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.dataSet:
            self.dataSet.remove(val)
            return True
        return False
        
    def getRandom(self) -> int:
        return random.sample(self.dataSet, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()