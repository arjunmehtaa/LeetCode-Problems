directions = [[-1,0], [1,0], [0,-1], [0,1]]

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights),  len(heights[0])
        atl = set()
        pac = set()
        ans = []
        
        def dfs(r, c, data, last):
            if r < 0 or c < 0 or r >= n or c >= m or (r, c) in data or heights[r][c] < last:
                return
            data.add((r, c))
            for d in directions:
                dfs(r + d[0], c + d[1], data, heights[r][c])
        
        for i in range(0, n):
            dfs(i, 0, pac, 0)
            dfs(i, m - 1, atl, 0)
            
        for j in range(0, m):
            dfs(0, j, pac, 0)
            dfs(n - 1, j, atl, 0)
                
        for i in range(0, n):
            for j in range(0, m):
                if (i, j) in atl and (i, j) in pac:
                    ans.append([i, j])
                    
        return ans
        