class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        flag = False
        a = 0
        b = len(s) - 1
        while a <= b:
            if s[a] != s[b]:
                a_removed = s[:a] + s[a+1:]
                b_removed = s[:b] + s[b+1:]
                if a_removed == a_removed[::-1] or b_removed == b_removed[::-1]:
                    return True
                else:
                    return False
            a += 1
            b -= 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# Optimal Solution
#
# Time Complexity: O(n)
# Space Complexity: O(1)

# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         a = 0
#         b = len(s) - 1
#         while a < b:
#             if s[a] != s[b]:
#                 x = s[a+1: b+1]
#                 y = s[a: b]
#                 return x == x[::-1] or y == y[::-1]
#             a += 1
#             b -= 1
#         return True