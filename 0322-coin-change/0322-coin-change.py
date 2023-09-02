class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        return traverse(amount, dp, coins)
            
def traverse(amount, dp, coins):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if amount not in dp:
        ans = inf
        for coin in coins:
            res = 1 + traverse(amount - coin, dp, coins)
            if res > 0:
                ans = min(ans, res)
        dp[amount] = ans
    return dp[amount] if dp[amount] != inf else -1

