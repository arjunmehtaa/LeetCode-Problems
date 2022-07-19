class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        if arr[0] > 1:
            k -= arr[0] - 1
        for i in range(0, len(arr) - 1):
            diff = arr[i+1] - arr[i] - 1
            if diff >= k:
                return arr[i] + k
            else:
                k -= diff
        return arr[len(arr)-1] + k