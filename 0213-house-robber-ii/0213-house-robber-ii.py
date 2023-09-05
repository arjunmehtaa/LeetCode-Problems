class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = nums[0]
        ans = max(ans, help(nums[:-1]), help(nums[1:]))
        return ans
        
def help(nums):
    one = 0
    two = 0
    for num in nums:
        temp = one
        one = two
        two = max(temp + num, two)
    return two