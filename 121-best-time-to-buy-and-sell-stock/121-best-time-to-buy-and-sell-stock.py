class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max = 0
        for i in range(0, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] - buy > max:
                max = prices[i] - buy
        return max