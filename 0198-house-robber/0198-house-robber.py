class Solution:
    def rob(self, nums: List[int]) -> int:
        one = 0
        two = 0
        for n in nums:
            temp = one
            one = two
            two = max(n + temp, two)
        return two