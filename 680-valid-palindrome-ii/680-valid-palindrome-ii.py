class Solution:
    def validPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) - 1
        while a <= b:
            if s[a] != s[b]:
                x = s[a + 1:b + 1]
                y = s[a:b]
                return x == x[::-1] or y == y[::-1]
            a += 1
            b -= 1
        return True