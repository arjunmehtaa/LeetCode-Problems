class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height) - 1
        area = 0
        while a < b:
            short = min(height[a], height[b])
            area = max(area, short*(b-a))
            if height[a] < height[b]:
                a += 1
            else: 
                b -= 1
        return area
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         answer = 0
#         a = 0
#         b = len(height) - 1
#         while(a!=b):     
#             area = min(height[a], height[b])*(b-a)
#             answer = max(answer, area)
#             if height[a] < height[b]:
#                 a += 1
#             else:
#                 b -= 1
#         return answer