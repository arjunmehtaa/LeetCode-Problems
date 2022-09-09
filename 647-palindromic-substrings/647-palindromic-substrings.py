class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        for i in range(0, len(s)):
            l = i 
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                answer += 1
                l -= 1
                r += 1
            l = i 
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                answer += 1
                l -= 1
                r += 1
        return answer