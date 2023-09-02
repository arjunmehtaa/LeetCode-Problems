class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = {}
        dp[0] = 0
        offset = 1
        for i in range(1, n + 1):
            if 2 * offset == i:
                offset *= 2
            dp[i] = 1 + dp[i - offset]
        return dp.values()
        