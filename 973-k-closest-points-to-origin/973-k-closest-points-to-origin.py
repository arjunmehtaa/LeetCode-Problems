class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        ans = []
        for x, y in points:
            dis = x*x + y*y
            res.append([dis, x, y])
        res.sort()
        for i in range(0, k):
            element = res[i]
            ans.append([element[1], element[2]])
        return ans