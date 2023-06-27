class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += countPalindrome(s, i, i)
            ans += countPalindrome(s, i, i + 1)
        return ans
        
def countPalindrome(s, a, b):
    ans = 0
    while a >= 0 and b < len(s) and s[a] == s[b]:
        ans += 1
        a -= 1
        b += 1
    return ans