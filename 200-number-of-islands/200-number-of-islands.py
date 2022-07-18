directions = [[-1,0], [0,1], [1,0], [0,-1]]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return False
        islands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                print("i,j is ", i, j)
                if grid[i][j] == "1":
                    islands += 1
                    grid[i][j] = "0"
                    queue = [[i,j]]
                    while len(queue) > 0:
                        pos = queue.pop(0)
                        row = pos[0]
                        col = pos[1]
                        for k in range(0, len(directions)):
                            current_dir = directions[k]
                            next_row = row + current_dir[0]
                            next_col = col + current_dir[1]
                            if next_row < 0 or next_col < 0 or next_row >= len(grid) or next_col >= len(grid[0]):
                                continue
                            if grid[next_row][next_col] == "1":
                                queue.append([next_row, next_col])
                                grid[next_row][next_col] = "0"
        return islands
                                
                                
                            
                        
    