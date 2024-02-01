class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = defaultdict(list)
        for word in strs:
            seen = [0] * 26
            for char in word:
                seen[ord(char) - ord('a')] += 1
            charMap[tuple(seen)].append(word)
        return charMap.values()
                