directions = [[-1,0], [1,0], [0,-1], [0,1]]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        fresh = 0
        queue = []
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append([i, j])
        rotten = len(queue)
        while len(queue) > 0:
            if rotten == 0:
                rotten = len(queue)
                mins += 1
            pos = queue.pop(0)
            rotten -= 1
            r, c = pos[0], pos[1]
            for direction in directions:
                nextRow = r + direction[0]
                nextCol = c + direction[1]
                if nextRow < 0 or nextCol < 0 or nextRow >= rows or nextCol >= cols:
                    continue
                if grid[nextRow][nextCol] == 1:
                    fresh -= 1
                    grid[nextRow][nextCol] = 2
                    queue.append([nextRow, nextCol])
        return mins if fresh <= 0 else -1