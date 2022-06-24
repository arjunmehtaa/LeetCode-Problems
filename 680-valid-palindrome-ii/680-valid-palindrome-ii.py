class Solution:
    def validPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) - 1
        flag = False
        while a < b:
            if s[a] != s[b]:
                x = s[a+1: b+1]
                y = s[a: b]
                if x == x[::-1] or y == y[::-1]:
                    return True
                else:
                    return False
            a += 1
            b -= 1
        return True
        