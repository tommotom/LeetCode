class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        ans = max(nums)
        q = [];
        for i, num in enumerate(nums):
            while q and i - q[0][1] > k:
                ans = max(ans, -heapq.heappop(q)[0])
            if q:
                last, j = heapq.heappop(q)
                heapq.heappush(q, (last-num, i))
                if num < 0: heapq.heappush(q, (last, j))
            heapq.heappush(q, (-num, i))
        if q:
            ans = max(ans, -heapq.heappop(q)[0])
        return ans
