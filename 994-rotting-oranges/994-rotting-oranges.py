directions = [[1,0], [-1,0], [0,1], [0,-1]]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        queue = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1
        rotten = len(queue)
        while len(queue) > 0:
            if rotten == 0:
                mins += 1
                rotten = len(queue)
            rotten -= 1
            orange = queue.pop(0)
            row = orange[0]
            col = orange[1]
            for direction in directions:
                nextRow = row + direction[0]
                nextCol = col + direction[1]
                if nextRow < 0 or nextCol < 0 or nextRow >= rows or nextCol >= cols:
                    continue
                if grid[nextRow][nextCol] == 1:
                    grid[nextRow][nextCol] = 2
                    queue.append([nextRow, nextCol])
                    fresh -= 1
        return mins if fresh == 0 else -1