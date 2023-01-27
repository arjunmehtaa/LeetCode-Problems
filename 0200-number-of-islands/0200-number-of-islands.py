directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            for d in directions:
                dfs(r + d[0], c + d[1])
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        
        return ans
                    