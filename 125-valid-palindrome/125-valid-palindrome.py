import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]+', '', s)
        s = s.lower()
        a = 0
        b = len(s) - 1
        while a <= b:
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True
        