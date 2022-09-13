class Solution:
    def minPartitions(self, n: str) -> int:
        maxDigit = 0
        for char in n:
            maxDigit = max(maxDigit, int(char))
            if maxDigit == 9:
                break
        return maxDigit
            