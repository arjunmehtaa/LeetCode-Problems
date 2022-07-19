directions = [[1,0], [-1,0], [0,1], [0,-1]]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = 0
        fresh = 0
        mins = 0
        queue = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 2:
                    rotten += 1
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1
        new_rotten = 0
        while len(queue) > 0:            
            if rotten == 0:
                mins += 1
                rotten = new_rotten
                new_rotten = 0
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
                    new_rotten += 1
                    fresh -= 1
        if fresh > 0:
            return -1
        return mins
                
                
                    
                    
# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         mins = 0
#         for i in range(0, len(grid)):
#             for j in range(0, len(grid[0])):
#                 if grid[i][j] == 2:
#                     grid[i][j] = 0
#                     queue = [[i, j]]
#                     while len(queue) > 0:
#                         mins += 1
#                         pos = queue.pop(0)
#                         row = pos[0]
#                         col = pos[1]
#                         for k in range(0, len(directions)):
#                             next_pos = directions[i]
#                             next_row = row + next_pos[0]
#                             next_col = col + next_pos[1]
#                             if next_row < 0 or next_col < 0 or next_row >= len(grid) or next_col >= len(grid[0]):
#                                 continue
#                             if grid[next_row][next_col] == 1:
#                                 queue.append([next_row, next_col])
#                                 grid[next_row][next_col] = 2
#         return mins + 1

