class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""
        
        answer = []
        maxLen = inf
        letters = {}
        window = {}
        
        for char in t:
            letters[char] = letters.get(char, 0) + 1
            
        have = 0
        need = len(letters)
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in letters and window[s[r]] == letters[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < maxLen:
                    maxLen = r - l + 1
                    answer = [l ,r]
                window[s[l]] -= 1
                if s[l] in letters and window[s[l]] < letters[s[l]]:
                    have -= 1
                l += 1
                
        return s[answer[0]:answer[1]+1] if maxLen < inf else ""
                