directions = [[-1,0], [1,0], [0,-1], [0,1]]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    islands += 1
                    queue = [[i, j]]
                    while len(queue) > 0:
                        pos = queue.pop(0)
                        row, col = pos[0], pos[1]
                        for direction in directions:
                            nextRow = row + direction[0]
                            nextCol = col + direction[1]
                            if nextRow < 0 or nextCol < 0 or nextRow >= rows or nextCol >= cols:
                                continue
                            if grid[nextRow][nextCol] == "1":
                                grid[nextRow][nextCol] = "0"
                                queue.append([nextRow, nextCol])
        return islands