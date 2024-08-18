class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], stealMoney(nums[1:]), stealMoney(nums[:len(nums) - 1]))
        
def stealMoney(nums):
    one, two = 0, 0
    for i in range(len(nums) - 1, -1, -1):
        temp = one
        one = max(nums[i] + two, one)
        two = temp
    return one
    