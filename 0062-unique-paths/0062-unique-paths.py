directions = [[-1, 0], [0, -1]]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        
        def traverse(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if (i, j) not in memo:
                memo[(i, j)] = 0
                for d in directions:
                    r = i + d[0]
                    c = j + d[1]
                    memo[(i, j)] += traverse(r, c)
            return memo[(i, j)]
                        
        return traverse(m - 1, n - 1)