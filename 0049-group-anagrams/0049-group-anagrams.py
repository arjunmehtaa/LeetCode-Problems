class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            charCount = [0] * 26
            for char in word:
                charCount[ord(char) - ord("a")] += 1
            group[tuple(charCount)].append(word)
        return group.values()