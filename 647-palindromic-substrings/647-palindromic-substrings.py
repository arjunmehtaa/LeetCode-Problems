class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = {}
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                string = s[i:j+1]
                if isPalindrome(s, i, j, dp):
                    count += 1
        return count
    
def isPalindrome(s, i, j, dp):
    if (i, j) in dp:
        return dp[(i, j)]
    if i >= j:
        return True
    if s[i] == s[j]:
        dp[(i, j)] = isPalindrome(s, i+1, j-1, dp)
        return dp[(i, j)]
    dp[(i, j)] = False
    return dp[(i, j)]
        
        