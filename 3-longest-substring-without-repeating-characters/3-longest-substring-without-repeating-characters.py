class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = 0
        map = {}
        ans = 0
        if len(s) <= 1:
            return len(s)
        for i in range(0, len(s)):
            if s[i] in map and map[s[i]] >= a:
                a = map[s[i]] + 1
            map[s[i]] = i
            ans = max(ans, i - a + 1)
        return ans
            
        
                
            
        