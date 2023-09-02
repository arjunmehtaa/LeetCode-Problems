class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tripleSum = nums[i] + nums[j] + nums[k]
                if tripleSum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j += 1
                elif tripleSum < 0:
                    j += 1
                else:
                    k -= 1
        return ans
    
[-1, 0, 1, 2, -1, -4]

[-4, -1, -1, 0, 1, 2]


            