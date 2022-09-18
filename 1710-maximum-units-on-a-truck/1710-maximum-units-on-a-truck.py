class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse = True, key = lambda i : i[1])
        ans = 0
        for num, units in boxTypes:
            if num > truckSize:
                ans += (truckSize * units)
                return ans
            else:
                ans += (num * units)
                truckSize -= num
        return ans
            