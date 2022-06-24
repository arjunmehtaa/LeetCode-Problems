import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]+', '', s)
        s = s.lower()
        a = 0
        b = len(s) - 1
        if s == s[::-1]:
            return True
        return False
        