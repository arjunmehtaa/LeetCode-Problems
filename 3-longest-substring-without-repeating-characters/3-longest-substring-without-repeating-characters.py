class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        seenMap = {}
        a = 0
        for b in range(0, len(s)):
            if s[b] in seenMap and seenMap[s[b]] >= a:
                a  = seenMap[s[b]] + 1
            seenMap[s[b]] = b
            answer = max(answer, b - a + 1)
        return answer
                
            