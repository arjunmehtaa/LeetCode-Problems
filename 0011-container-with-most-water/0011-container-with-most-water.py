class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height) - 1
        amount = 0
        while a < b:
            area = (b - a) * min(height[a], height[b])
            amount = max(amount, area)
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
        return amount
        