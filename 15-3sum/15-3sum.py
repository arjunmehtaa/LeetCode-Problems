class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return ans
        
        
        
        
        # map = {}
        # ans = []
        # for i in range(0 ,len(nums)):
        #     sum_to_find = 0 - nums[i]
        #     map[sum_to_find] = i
        # for i in range(0 ,len(nums)):
        #     for j in range(0 ,len(nums)):
        #         sub = nums[i] + nums[j]
        #         if i != j and sub in map and map[sub] != i and map[sub] != j:
        #             arr = [-sub, nums[i], nums[j]]
        #             arr.sort()
        #             if arr not in ans:
        #                 ans.append(arr)
        # return ans
    
        