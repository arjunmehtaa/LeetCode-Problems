class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key = lambda i : i[0])
        for i in range(len(intervals)):
            if i > 0 and intervals[i][0] <= ans[-1][1]:
                end = max(ans[-1][1], intervals[i][1])
                ans[-1][1] = end
            else:
                ans.append(intervals[i])
        return ans