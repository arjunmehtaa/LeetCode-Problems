class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                string = s[i:j+1]
                if string == string[::-1]:
                    count += 1
        return count
        