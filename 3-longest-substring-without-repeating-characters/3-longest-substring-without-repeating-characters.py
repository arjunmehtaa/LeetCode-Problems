# Optimal Solution
#
# Time Complexity   :   O(N)
# Space Complexity  :   O(N)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        answer = 0
        data = {}
        a = 0
        for b in range(0, len(s)):
            if s[b] in data and data[s[b]] >= a:
                a = data[s[b]] + 1
            data[s[b]] = b
            answer = max(answer, b - a + 1)
        return answer           

# Brute Force Solution
#
# Time Complexity   :   O(N^2)
# Space Complexity  :   O(N)
#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) <= 1:
#             return len(s)
#         answer = 0
#         for i in range(0, len(s)):
#             data = set()
#             j = i
#             while j < len(s) and s[j] not in data:
#                 data.add(s[j])
#                 j += 1
#                 answer = max(answer, len(data))
#         return answer