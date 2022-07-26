# Optimal Solution

class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        a = 0
        b = len(height) - 1
        max_l = 0
        max_r = 0
        while(a != b):
            if height[a] <= height[b]:
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
    
# Brute Force Solution

# class Solution:
# def trap(self, height: List[int]) -> int:
#     total = 0
#     for i in range(0, len(height)):
#         max_l = 0
#         max_r = 0
#         for j in range(0,len(height)):
#             if j < i and height[j] > max_l:
#                 max_l = height[j]     
#             if j > i and height[j] > max_r:
#                 max_r = height[j]
#         water_level = min(max_l, max_r) - height[i]
#         if water_level > 0:
#             total += water_level
#     return total