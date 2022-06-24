# Optimal Solution
#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 1:
#             return 1
#         else:
#             answer = 0
#             data = set()
#             a = 0
#             b = 0
#             while b < len(s):
#                 if s[b] in data:
#                     data.remove(s[a])
#                     a += 1
#                     answer = max(answer, len(data))
#                 else:
#                     data.add(s[b])
#                     b += 1
#                     answer = max(answer, len(data))
#         return answer
            
            

# Brute Force Solution
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        answer = 0
        for i in range(0, len(s)):
            data = set()
            j = i
            while j < len(s) and s[j] not in data:
                data.add(s[j])
                j += 1
                answer = max(answer, len(data))
        return answer
        