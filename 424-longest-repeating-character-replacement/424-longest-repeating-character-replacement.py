class Solution:
    def characterReplacement(self, s: str, k: int) -> int:       
        seen = {}
        answer = 0
        a = 0
        maxCount = 0
        for b in range(len(s)):
            if s[b] in seen:
                seen[s[b]] += 1
            else:
                seen[s[b]] = 1
            maxCount = max(maxCount, seen[s[b]])
            while (b - a - maxCount + 1) > k:
                seen[s[a]] -= 1
                a += 1
            answer = max(answer, b - a + 1)
        return answer
