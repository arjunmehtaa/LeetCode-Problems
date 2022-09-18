class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse = True, key = lambda i : i[1])
        ans = 0
        total = 0
        while len(boxTypes) > 0 and total < truckSize:
            total += 1
            ans += boxTypes[0][1]
            boxTypes[0][0] -= 1
            if boxTypes[0][0] == 0:
                boxTypes.pop(0)
        return ans
            