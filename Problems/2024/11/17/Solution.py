class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = float("inf")
        cum = 0
        q = []

        for i, num in enumerate(nums):
            cum += num
            if cum >= k: ans = min(ans, i + 1)
            while q and cum - q[0][0] >= k:
                ans = min(ans, i - heappop(q)[1])
            heappush(q, (cum, i))
        return -1 if ans == float("inf") else ans
