directions = [[0,1], [1,0], [0,-1], [-1,0]]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        size = len(matrix)*len(matrix[0])
        ans = []
        i = 0
        j = 0
        queue = []
        counter = 0
        finished = False
        while not finished:
            for direction in directions:
                counter += 1
                queue = [[i, j]]
                while len(queue) > 0:
                    element = queue.pop(0)
                    row = element[0]
                    col = element[1]
                    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
                        continue
                    if not seen[row][col]:
                        ans.append(matrix[row][col])
                        if len(ans) == size:
                            finished = True
                        seen[row][col] = True
                        i = row
                        j = col
                    queue.append([row + direction[0], col + direction[1]])
        return ans
    
    
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