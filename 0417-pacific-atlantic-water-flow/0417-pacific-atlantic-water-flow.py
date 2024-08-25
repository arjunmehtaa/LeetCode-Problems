directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=  len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        
        def dfs(i, j, visit):
            visit.add((i, j))
            for d in directions:
                r = i + d[0]
                c = j + d[1]
                if r >= 0 and c >= 0 and r < rows and c < cols and heights[r][c] >= heights[i][j] and (r, c) not in visit:
                    dfs(r, c, visit)
                    
        for i in range(rows):
            dfs(i, 0, pac)
            dfs(i, cols - 1, atl)
            
        for j in range(cols):
            dfs(0, j, pac)
            dfs(rows - 1, j, atl)
            
        return atl.intersection(pac)
            