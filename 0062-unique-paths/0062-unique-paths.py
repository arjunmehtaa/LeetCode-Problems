directions = [[1, 0], [0, 1]]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {}
        return dfs(0, 0, m, n, mem)
        
def dfs(x, y, m, n, mem):
    if x == m - 1 and y == n - 1:
        return 1
    if x > m - 1 or y > n - 1:
        return 0
    if (x, y) not in mem:
        count = 0
        for direction in directions:
            count += dfs(x + direction[0], y + direction[1], m , n, mem)
        mem[(x, y)] = count
    return mem[(x, y)]
        