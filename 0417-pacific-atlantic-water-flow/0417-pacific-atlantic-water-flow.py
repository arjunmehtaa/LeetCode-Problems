directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        rows = len(heights)
        cols = len(heights[0])
        
        def traverse(i, j, visit):
            visit.add((i, j))
            for d in directions:
                r = i + d[0]
                c = j + d[1]
                if r >= 0 and c >= 0 and r < rows and c < cols and (r, c) not in visit and heights[r][c] >= heights[i][j]:
                    traverse(i + d[0], j + d[1], visit)
                
        for i in range(rows):
            traverse(i, 0, pac)
            traverse(i, cols - 1, atl)
            
        for j in range(cols):
            traverse(0, j, pac)
            traverse(rows - 1, j, atl)
            
        return atl.intersection(pac)