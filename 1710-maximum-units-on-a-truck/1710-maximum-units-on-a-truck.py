class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse = True, key = lambda i : i[1])
        ans = 0
        for num, units in boxTypes:
            if truckSize == 0:
                break
            if num > truckSize:
                ans += (truckSize * units)
                truckSize = 0
            else:
                ans += (num * units)
                truckSize -= num
        return ans
            