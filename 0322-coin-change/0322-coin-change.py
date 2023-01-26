class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        def traverse(amountRemain, memo):
            if amountRemain == 0:
                return 0
            if amountRemain < 0:
                return -1
            if amountRemain not in memo:
                ans = inf
                for coin in coins:
                    value = traverse(amountRemain - coin, memo)
                    if value > -1 and value < ans:
                        ans = value
                memo[amountRemain] = 1 + ans if ans != inf else -1
            return memo[amountRemain]
        
        memo = {}
        return traverse(amount, memo)