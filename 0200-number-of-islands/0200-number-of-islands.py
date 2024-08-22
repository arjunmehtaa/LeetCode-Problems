# Time Complexity   : O(M X N) 		(It is O(2N) because even though we might end up traversing through 
#					                the entire grid, we would never encounter that island again)
# Space Complexity  : O(max(M, N))	(where matrix is N X M)

directions = [[-1,0], [0,1], [1,0], [0,-1]]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return False
        islands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    grid[i][j] = "0"
                    queue = [[i,j]]
                    while len(queue) > 0:
                        pos = queue.pop(0)
                        row = pos[0]
                        col = pos[1]
                        for k in range(0, len(directions)):
                            current_dir = directions[k]
                            next_row = row + current_dir[0]
                            next_col = col + current_dir[1]
                            if next_row < 0 or next_col < 0 or next_row >= len(grid) or next_col >= len(grid[0]):
                                continue
                            if grid[next_row][next_col] == "1":
                                queue.append([next_row, next_col])
                                grid[next_row][next_col] = "0"
        return islands                     
    
    
    
# directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:    
#         ans = 0
#         rows = len(grid)
#         cols = len(grid[0])
        
#         def traverse(i, j):
#             if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != "1":
#                 return
#             grid[i][j] = 0
#             for d in directions:
#                 r = i + d[0]
#                 c = j + d[1]
#                 traverse(r, c)
            
            
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == "1":
#                     traverse(i, j)
#                     ans += 1
                    
#         return ans
                    