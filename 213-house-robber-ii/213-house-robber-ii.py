class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], robHouse(nums[1:]), robHouse(nums[:len(nums) - 1]))
        
def robHouse(nums):
    rob1 = 0 
    rob2 = 0
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2