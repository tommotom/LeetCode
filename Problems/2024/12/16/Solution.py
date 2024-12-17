class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        q = []
        for i, num in enumerate(nums):
            heapq.heappush(q, (num, i))

        for _ in range(k):
            num, i = heapq.heappop(q)
            heapq.heappush(q, (num * multiplier, i))

        ans = [0 for _ in range(len(nums))]
        while q:
            num, i = heapq.heappop(q)
            ans[i] = num

        return ans
