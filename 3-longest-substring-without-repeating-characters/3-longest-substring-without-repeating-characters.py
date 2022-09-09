class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        seenMap = {}
        answer = 1
        a = 0
        
        for b in range(len(s)):
            if s[b] in seenMap and seenMap[s[b]] >= a:
                a = seenMap[s[b]] + 1
            seenMap[s[b]] = b
            answer = max(answer, b - a + 1)
            
        return answer