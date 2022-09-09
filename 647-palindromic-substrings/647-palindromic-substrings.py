# Time Complexity	: O(N^2)
# Space Complexity	: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        for i in range(0, len(s)):
            answer += countPalindromes(s, i, i)
            answer += countPalindromes(s, i, i + 1)
        return answer
    
def countPalindromes(s, l, r):
    answer = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        answer += 1
        l -= 1
        r += 1
    return answer