class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        h = [(-nums[n-1], n-1)]
        for cur in range(n-2, -1, -1):
            while cur + k < h[0][1]:
                heapq.heappop(h)
            heapq.heappush(h, (h[0][0] - nums[cur], cur))
        while h[0][1] > 0:
            heapq.heappop(h)
        return -h[0][0]
