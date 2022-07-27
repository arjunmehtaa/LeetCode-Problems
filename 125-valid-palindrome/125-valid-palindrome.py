import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]+', '', s)
        s = s.lower()
        return s == s[::-1]
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # import re

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = re.sub('[^A-Za-z0-9]+', '', s)
#         s = s.lower()
#         if s == s[::-1]:
#             return True
#         return False