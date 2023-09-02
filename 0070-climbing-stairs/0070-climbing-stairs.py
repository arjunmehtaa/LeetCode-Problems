class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 2
        if n <= 1:
            return n
        for i in range(n - 3, -1, -1):
            temp = two
            two = two + one
            one = temp
        return two
            
        
# | 5 |    | 3 |   | 2 |   | 1 |