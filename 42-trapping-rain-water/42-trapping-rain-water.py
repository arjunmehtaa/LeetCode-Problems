class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = 0
        max_r = 0
        total = 0
        a = 0
        b = len(height) - 1
        while a < b:
            if height[a] < height[b]:
                if height[a] > max_l:
                    max_l = height[a]
                elif height[a] < max_l:
                    total += max_l - height[a]
                a += 1
            else:
                if height[b] > max_r:
                    max_r = height[b]
                elif height[b] < max_r:
                    total += max_r - height[b]
                b -= 1
        return total
                    
        