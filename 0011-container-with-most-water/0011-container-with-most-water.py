class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height) - 1
        ans = 0
        while a < b:
            area = (b - a) * min(height[a], height[b])
            ans = max(ans, area)
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
        return ans