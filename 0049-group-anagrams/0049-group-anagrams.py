# Let N be average length of word and M words

# Optimal Solution
# Time Complexity	: O(M * N * 26)
# Space Complexity	: O(M * N * 26)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            answer[tuple(count)].append(word)
        return answer.values()

    
# Brute Force Solution
# Time Complexity	: O(M * N LOG(N))
# Space Complexity	: O(M * N)

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagramMap = {}
#         for word in strs:
#             sortedWord = "".join(sorted(word))
#             if sortedWord in anagramMap:
#                 anagramMap[sortedWord].append(word)
#             else:
#                 anagramMap[sortedWord] = [word]
#         return anagramMap.values()
        
