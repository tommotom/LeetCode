class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        q = []
        for g in gifts:
            heapq.heappush(q, -g)

        for _ in range(k):
            g = -heapq.heappop(q)
            heapq.heappush(q, math.ceil(-math.sqrt(g)))

        return -sum(q)
