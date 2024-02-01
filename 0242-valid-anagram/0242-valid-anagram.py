class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}
        for char in s:
            charMap[char] = charMap.get(char, 0) + 1
        for char in t:
            if char not in charMap:
                return False
            charMap[char] -= 1
            if charMap[char] == 0:
                del charMap[char]
        return len(charMap) == 0