directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])
        ans = []
        pac = set()
        atl = set()
        
        def traverse(i, j, visit):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visit:
                return
            visit.add((i, j))
            for d in directions:
                r = i + d[0]
                c = j + d[1]
                if r >= 0 and c >= 0 and r < rows and c < cols and (r, c) not in visit and  heights[r][c] >= heights[i][j]:
                    traverse(r, c, visit)
                    
        for i in range(rows):
            traverse(i, 0, pac)
            traverse(i, cols - 1, atl)
            
        for j in range(cols):
            traverse(0, j, pac)
            traverse(rows - 1, j, atl)
            
        for (a, b) in pac:
            if (a, b) in atl and [a, b] not in ans:
                ans.append([a, b])
                
        return ans
                    
        