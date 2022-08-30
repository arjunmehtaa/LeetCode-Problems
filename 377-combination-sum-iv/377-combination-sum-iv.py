class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0
        ans = 0
        memo = {}
        for num in nums:
            res += dfs(nums, num, ans, target, memo)
        return res
        
def dfs(nums, num, ans, target, memo):
    ans += num
    if ans == target:
        return 1
    elif ans > target:
        return 0
    if (num, ans) not in memo:
        count = 0
        for n in nums:
            count += dfs(nums, n, ans, target, memo)
        memo[(num, ans)] = count
    return memo[(num, ans)]
        