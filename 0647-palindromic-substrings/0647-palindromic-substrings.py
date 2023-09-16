# Time Complexity	: O(N^2)
# Space Complexity	: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        for i in range(0, len(s)):
            answer += countPalindromes(s, i, i)
            answer += countPalindromes(s, i, i + 1)
        return answer
    
def countPalindromes(s, l, r):
    answer = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        answer += 1
        l -= 1
        r += 1
    return answer

# ENCODE AND DECODE STRINGS SOLUTION

# class Solution:
#     """
#     @param: strs: a list of strings
#     @return: encodes a list of strings to a single string.
#     """
#     def encode(self, strs):
#         # write your code here
#         result = ""
#         for s in strs:
#             result += str(len(s)) + "#" + s
#         return result
#     """
#     @param: str: A string
#     @return: dcodes a single string to a list of strings
#     """
#     def decode(self, str):
#         # write your code here
#         result = []
#         i = 0
#         while i < len(str):
#             j = i
#             while str[j] != "#":
#                 j += 1
#             length = int(str[i:j])
#             result.append(str[j + 1: j + 1 + length])
#             i = j + 1 + length
#         return result