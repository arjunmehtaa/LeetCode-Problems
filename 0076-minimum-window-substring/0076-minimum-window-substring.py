class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        window = {}
        countT = {}
        ans = [-1, -1]
        ansLen = inf
        
        for c in t:
            countT[c] = countT.get(c, 0) + 1
            
        have = 0
        need = len(countT)
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if r - l + 1 < ansLen:
                    ansLen = r - l + 1
                    ans = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
           
        return s[ans[0]: ans[1] + 1] if ansLen < inf else ""
    