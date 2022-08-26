class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        dict = {}
        a = 0
        b = 0
        answer = 0
        while b < len(s):
            if s[b] in dict and dict[s[b]] >= a:
                a = dict[s[b]] + 1
            dict[s[b]] = b
            answer = max(answer, b - a + 1)
            b += 1
        return answer
        
        