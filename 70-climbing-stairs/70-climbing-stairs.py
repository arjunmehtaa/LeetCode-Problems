class Solution:
    def climbStairs(self, n: int) -> int:
        one = 2
        two = 1
        if n <= 1:
            return n
        for i in range(n - 3,-1, -1):
            temp = one
            one = one + two
            two = temp
        return one