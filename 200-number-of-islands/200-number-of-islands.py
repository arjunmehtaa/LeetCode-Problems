directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        answer = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1":
                    answer += 1
                    grid[i][j] = "0"
                    queue = [[i, j]]
                    while len(queue) > 0:
                        element = queue.pop(0)
                        row = element[0]
                        col = element[1]
                        for direction in directions:
                            next_row = row + direction[0]
                            next_col = col + direction[1]
                            if next_row < 0 or next_col < 0 or next_row >= len(grid) or next_col >= len(grid[0]):
                                continue
                            if grid[next_row][next_col] == "1":
                                queue.append([next_row, next_col])
                                grid[next_row][next_col] = "0"
        return answer
                    
        