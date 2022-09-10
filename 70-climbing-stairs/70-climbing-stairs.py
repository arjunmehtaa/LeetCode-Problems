class Solution:
    def climbStairs(self, n: int) -> int:
        memo= {}
        return dfs(n, memo)
    
def dfs(n, memo):
    if n <= 2:
        return n
    if n not in memo:
        memo[n] = dfs(n-1, memo) + dfs(n-2, memo)
    return memo[n]