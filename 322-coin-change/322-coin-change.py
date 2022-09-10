class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        return dfs(coins, amount, memo)
        
def dfs(coins, amountLeft, memo):
    if amountLeft < 0:
        return -1
    if amountLeft == 0:
        return 0
    if amountLeft not in memo:
        answer = inf
        for coin in coins:
            value = dfs(coins, amountLeft - coin, memo)
            if value > -1 and value < answer:
                answer = value
        memo[amountLeft] = 1 + answer if answer != inf else -1
    return memo[amountLeft]