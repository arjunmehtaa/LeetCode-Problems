directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        
        def traverse(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            for d in directions:
                traverse(i + d[0], j + d[1])
                
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    traverse(i, j)
                    ans += 1
                    
        return ans