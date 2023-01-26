class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def traverse(amountLeft, memo):
            if amountLeft == 0:
                return 0
            if amountLeft < 0:
                return -1
            if amountLeft not in memo:
                ans = inf
                for coin in coins:
                    value = traverse(amountLeft - coin, memo)
                    if value > -1 and value < ans:
                        ans = value
                memo[amountLeft] = 1 + ans if ans < inf else -1
            return memo[amountLeft]
        
        memo = {}
        return traverse(amount, memo)