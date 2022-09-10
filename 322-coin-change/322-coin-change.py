# Bottom - Up 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1 
        
        
# Top - Down Memoization
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         memo = {}
#         return dfs(coins, amount, memo)
        
# def dfs(coins, amountLeft, memo):
#     if amountLeft < 0:
#         return -1
#     if amountLeft == 0:
#         return 0
#     if amountLeft not in memo:
#         answer = inf
#         for coin in coins:
#             value = dfs(coins, amountLeft - coin, memo)
#             if value > -1 and value < answer:
#                 answer = value
#         memo[amountLeft] = 1 + answer if answer != inf else -1
#     return memo[amountLeft]