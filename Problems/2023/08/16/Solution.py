class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, ans = [], []
        for i, num in enumerate(nums):
            heapq.heappush(q, (-num, i))
            while q and i - q[0][1] >= k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans[k-1:]
