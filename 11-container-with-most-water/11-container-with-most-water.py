class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height) - 1
        answer = 0
        while a < b:
            area = min(height[a], height[b]) * (b - a)
            answer = max(answer, area)
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
        return answer
        