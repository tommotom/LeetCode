import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        for i in range(k):
            heapq.heappush(h, (-nums[i], i))

        ans = []
        for i in range(k, len(nums)):
            while h[0][1] < i-k: heapq.heappop(h)
            ans.append(-h[0][0])
            heapq.heappush(h, (-nums[i], i))
        while h[0][1] < len(nums)-k: heapq.heappop(h)
        ans.append(-h[0][0])
        return ans
