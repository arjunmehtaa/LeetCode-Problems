class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        freqs = [[] for _ in range(len(nums) + 1)]
        answer = []
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
        for key in countMap:
            freqs[countMap[key]].append(key)
        print(freqs)
        for i in range(len(freqs) - 1, -1, -1):
            if len(freqs[i]) > 0:
                answer.extend(freqs[i])
                k -= len(freqs[i])
            if k <= 0:
                break
        return answer
            