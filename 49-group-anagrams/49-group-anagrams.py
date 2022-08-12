class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        map = {}
        for i in range(0, len(strs)):
            s = strs[i]
            s = ''.join(sorted(s))
            if s in map:
                map[s].append(strs[i])
            else:
                map[s] = [strs[i]]
        for key in map:
            ans.append(map[key])
        return ans