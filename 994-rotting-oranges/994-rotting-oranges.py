# Time Complexity   : O(N)
# Space Complexity  : O(N)
# where N = A x B for an A x B matrix (N is number of total elements in the grid)

directions = [[1,0], [-1,0], [0,1], [0,-1]]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        mins = 0
        queue = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1
        rotten = len(queue)
        new_rotten = 0
        while len(queue) > 0:            
            if rotten == 0:
                mins += 1
                rotten = len(queue)
            rotten -= 1
            pos = queue.pop(0)
            row = pos[0]
            col = pos[1]
            for direction in directions:
                next_row = row + direction[0]
                next_col = col + direction[1]
                if next_row < 0 or next_col < 0 or next_row >= len(grid) or next_col >= len(grid[0]):
                    continue
                if grid[next_row][next_col] == 1:
                    grid[next_row][next_col] = 2
                    queue.append([next_row, next_col])
                    fresh -= 1
        if fresh > 0:
            return -1
        return mins
