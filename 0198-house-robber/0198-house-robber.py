class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        
        def traverse(index):
            if index not in dp:
                if (n - index) == 1:
                    dp[index] = nums[index]
                elif (n - index) == 2:
                    dp[index] = max(nums[index:])
                else:
                    dp[index] = nums[index] + dp[index + 2]
                    if index + 3 < len(nums):
                        dp[index] = max(dp[index], nums[index] + dp[index + 3])
            return dp[index]
        
        
        for i in range(len(nums) - 1, -1, -1):
            traverse(i)
                        
        return max(dp.values())
        
        
        
        
        
        