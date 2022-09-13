class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexMap = {}
        answer = 0
        a = 0
        for b in range(len(s)):
            if s[b] in indexMap and indexMap[s[b]] >= a:
                a = indexMap[s[b]] + 1
            indexMap[s[b]] = b
            answer = max(answer, b - a + 1)
        return answer
        