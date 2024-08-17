# Let heights be an M x N matrix
# Time Complexity	: O(M x N)
# Space Complexity	: O(M x N)

directions = [[-1,0], [1,0], [0,-1], [0,1]]

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        result = []
        
        def dfs(r, c, visit, prevHeight):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visit or 
                heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            for direction in directions:
                next_row = r + direction[0]
                next_col = c + direction[1]
                dfs(next_row, next_col, visit, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
            
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
            
        return list(pac.intersection(atl))
        