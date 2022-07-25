directions = [[-1,-2], [-1,2], [-2,-1], [-2,1], [1,-2], [1,2], [2,-1], [2,1]]

# Better Solution (Recursion + Memoization)
#
# Time Complexity   : O(N^2 * K)
# Space Complexity  : O(N^2 * K)
#
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[None for _ in range(n)] for _ in range(n)] for _ in range(k+1)]
        return recurse(n, k, row, column, dp)

def recurse(n, k, row, column, dp):
    if row < 0 or column < 0 or row >= n or column >= n:
        return 0
    if k == 0:
        return 1
    if dp[k][row][column] != None:
        return dp[k][row][column]
    res = 0
    for direction in directions:
        res += recurse(n, k-1, row + direction[0], column + direction[1], dp) / 8
    dp[k][row][column] = res
    return dp[k][row][column]
        
# Initial Solution (Recursion)
#
# Time Complexity   : O(8^K)
# Space Complexity  : O(8^K)
#
# class Solution:
#     def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
#         if row < 0 or column < 0 or row >= n or column >= n:
#             return 0
#         if k == 0:
#             return 1
#         res = 0
#         for direction in directions:
#             res += self.knightProbability(n, k-1, row + direction[0], column + direction[1]) / 8
#         return res