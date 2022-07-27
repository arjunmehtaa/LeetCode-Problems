class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        a = 0
        b = 0
        max_len = 1
        seen = {}
        while b < len(s):
            if s[b] in seen and seen[s[b]] >= a:
                a = seen[s[b]] + 1
                seen[s[b]] = b
            else:
                seen[s[b]] = b
            max_len = max(max_len, b-a+1)
            b += 1
        return max_len
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# Optimal Solution
#
# Time Complexity   :   O(N)
# Space Complexity  :   O(N)

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) <= 1:
#             return len(s)
#         answer = 0
#         data = {}
#         a = 0
#         for b in range(0, len(s)):
#             if s[b] in data and data[s[b]] >= a:
#                 a = data[s[b]] + 1
#             data[s[b]] = b
#             answer = max(answer, b - a + 1)
#         return answer           

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