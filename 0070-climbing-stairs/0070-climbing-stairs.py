class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
        
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memo = {}
        
#         def traverse(index):
#             if index == 0:
#                 return 1
#             if index < 0:
#                 return 0
#             if index not in memo:
#                 memo[index] = traverse(index - 1) + traverse(index - 2)
#             return memo[index]
        
#         return traverse(n)
        