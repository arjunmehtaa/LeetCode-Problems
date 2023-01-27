directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    queue = [[i, j]]
                    ans += 1
                    while len(queue):
                        val = queue.pop(0)
                        r, c = val[0], val[1]
                        for d in directions:
                            row, col = r + d[0], c + d[1]
                            if row < 0 or col < 0 or row >= n or col >= m:
                                continue
                            if grid[row][col] == "1":
                                queue.append([row, col])
                                grid[row][col] = "0"
                
        return ans
                    