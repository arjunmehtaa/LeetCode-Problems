class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        ans = []
        map = {}
        for point in points:
            x, y = point[0], point[1]
            dis = x*x + y*y
            res.append([dis, x, y])
        res.sort()
        i = 0
        while i < k:
            element = res[i]
            i += 1
            ans.append([element[1], element[2]])
        return ans