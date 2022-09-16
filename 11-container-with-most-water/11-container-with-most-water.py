class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        a = 0
        b = len(height) - 1
        while a < b:
            area = min(height[a], height[b]) * (b - a)
            maxWater = max(maxWater, area)
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
        return maxWater