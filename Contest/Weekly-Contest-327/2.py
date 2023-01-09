class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, -num)

        score = 0
        for _ in range(k):
            num = -heapq.heappop(q)
            score += num
            heapq.heappush(q, -ceil(num/3))

        return score
