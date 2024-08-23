class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(remainingAmount):
            if remainingAmount == 0:
                return 0
            if remainingAmount < 0:
                return inf
            if remainingAmount not in memo:
                memo[remainingAmount] = inf
                for c in coins:
                    memo[remainingAmount] = min(memo[remainingAmount], 1 + dfs(remainingAmount - c))
            return memo[remainingAmount]
        
        result = dfs(amount)
        return result if result != inf else -1
                