class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        ans = 0
        for i in range(0, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            profit = prices[i] - buy
            ans = max(ans, profit)
        return ans