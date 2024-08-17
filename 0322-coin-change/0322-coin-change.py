class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for i in range(amount + 1)]
        for i in range(1, amount + 1):
            ans = inf
            for c in coins:
                diff = i - c
                if diff > 0:
                    diff_ans = dp[diff]
                    if diff_ans >= 0:
                        ans = min(ans, 1 + dp[diff])
                elif diff == 0:
                    ans = 1
            dp[i] = ans if ans < inf else -1
        return dp[amount] if amount > 0 else 0
                    
                    