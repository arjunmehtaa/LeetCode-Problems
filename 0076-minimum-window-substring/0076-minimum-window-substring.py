class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]
        resLen = float("infinity")
        tMap = {}
        sMap = {}
        for char in t:
            tMap[char] = tMap.get(char, 0) + 1
        a = 0
        have = 0
        need = len(tMap)
        for b in range(len(s)):
            sMap[s[b]] = sMap.get(s[b], 0) + 1
            if s[b] in tMap and sMap[s[b]] == tMap[s[b]]:
                have += 1
            while need == have:
                if (b - a + 1) < resLen:
                    resLen = b - a + 1
                    res = [a, b]
                sMap[s[a]] -= 1
                if s[a] in tMap and sMap[s[a]] < tMap[s[a]]:
                    have -= 1
                a += 1
        return s[res[0]:res[1] + 1] if resLen != float("infinity") else ""