class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        last = 1
        secondLast = 2
        for i in range(n - 3, -1, -1):
            temp = secondLast
            secondLast += last
            last = temp
        return secondLast