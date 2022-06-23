class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        else:
            answer = 0
            data = set()
            a = 0
            b = 0
            while b < len(s):
                if s[b] in data:
                    data.remove(s[a])
                    a += 1
                    answer = max(answer, len(data))
                else:
                    data.add(s[b])
                    b += 1
                    answer = max(answer, len(data))
        return answer
            
            

# Brute Force Solution
#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         answer = 0
#         if len(s) == 1:
#             return 1
#         else:
#             for i in range(0, len(s) - 1):
#                 data = set()
#                 data.add(s[i])
#                 j = i + 1
#                 count = 1
#                 while j < len(s) and s[j] not in data:
#                     data.add(s[j])
#                     count += 1
#                     j += 1
#                 answer = max(answer, count)
#         return answer
        