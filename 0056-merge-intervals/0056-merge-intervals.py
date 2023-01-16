class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            lastEnd = ans[-1][1]
            if intervals[i][0] <= lastEnd:
                end = max(lastEnd, intervals[i][1])
                ans[-1][1] = end
            else:
                ans.append(intervals[i])
        return ans