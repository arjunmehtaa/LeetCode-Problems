class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = len(s)
        offset = 1
        while offset < len(s):
            for a in range(len(s) - offset):
                if isPalindrome(s[a: a + offset + 1]):
                    answer += 1
            offset += 1
        return answer
            
def isPalindrome(s) -> bool:
    return s == s[::-1]