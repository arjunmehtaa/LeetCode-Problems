directions = [[1, 0], [0, 1]]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        return dfs(0, 0, m, n, memo)
        
def dfs(x, y, m, n, memo):
    if x < 0 or y < 0 or x >= m or y >= n:
        return 0
    if x == m - 1 and y == n - 1:
        return 1
    if (x, y) not in memo:
        res = 0
        for direction in directions:
            row = x + direction[0]
            col = y + direction[1]
            res += dfs(row, col, m, n, memo)
        memo[(x, y)] = res
    return memo[(x, y)]
        
        