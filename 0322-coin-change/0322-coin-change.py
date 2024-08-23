class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for amt in range(1, amount + 1):
            for c in coins:
                diff = amt - c
                if diff >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[diff])
        return dp[amount] if dp[amount] != (amount + 1) else -1
                    