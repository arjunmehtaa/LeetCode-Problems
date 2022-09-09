# Optimal Solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        total = len(matrix) * len(matrix[0])
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        ans = []
        while len(ans) < total:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1  
        return ans[:total]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
# Brute Force Solution
# directions = [[0,1], [1,0], [0,-1], [-1,0]]

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         total = len(matrix)*len(matrix[0]) - 1
#         ans = [matrix[0][0]]
#         row, col = 0, 0
#         seen = set()
#         seen.add((0, 0))
#         while total > 0:
#             for direction in directions:
#                 row += direction[0]
#                 col += direction[1]
#                 while (row >= 0 
#                        and col >= 0 
#                        and row < len(matrix) 
#                        and col < len(matrix[0]) 
#                        and (row, col) not in seen):
#                     ans.append(matrix[row][col])
#                     total -= 1
#                     seen.add((row, col))
#                     row += direction[0]
#                     col += direction[1]
#                 row -= direction[0]
#                 col -= direction[1]
#         return ans
                    
        
# # BFS in 2D Array

# # Time Complexity   : O(N)
# # Space Complexity  : O(N)

# # Note: If values are allowed to be duplicate, seen functionality would have to change
# # to a an array of boolean values, where we can check if seen[i][j] is true

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         seen = set()
#         ans = []
#         queue = [[0,0]]
#         while len(queue) > 0:
#             position = queue.pop(0)
#             i = position[0]
#             j = position[1]
#             if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] in seen:
#                 continue
#             ans.append(matrix[i][j])
#             seen.add(matrix[i][j])
#             queue.append([i-1, j])
#             queue.append([i, j+1])
#             queue.append([i+1, j])
#             queue.append([i, j-1])
#         print(ans)