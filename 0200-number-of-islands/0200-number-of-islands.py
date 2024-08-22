directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    ans += 1
                    queue = [[i, j]]
                    while len(queue):
                        r, c = queue.pop(0)
                        for d in directions:
                            nextRow = r + d[0]
                            nextCol = c + d[1]
                            if nextRow >= 0 and nextCol >= 0 and nextRow < rows and nextCol < cols and grid[nextRow][nextCol] == "1":
                                grid[nextRow][nextCol] = "0"
                                queue.append([nextRow, nextCol])
        return ans
                