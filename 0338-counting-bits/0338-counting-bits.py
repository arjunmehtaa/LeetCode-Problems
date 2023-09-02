class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n + 1):
            res = 0
            while i:
                res += i % 2
                i = i >> 1
            ans.append(res)
        return ans
        