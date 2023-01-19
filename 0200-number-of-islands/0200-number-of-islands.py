directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ans += 1
                    queue = [[i, j]]
                    while len(queue):
                        ele = queue.pop(0)
                        for direction in directions:
                            r = ele[0] + direction[0]
                            c = ele[1] + direction[1]
                            if r < 0 or c < 0 or r >= n or c >= m:
                                continue
                            if grid[r][c] == "1":
                                grid[r][c] = "0"
                                queue.append([r, c])
        return ans
                        