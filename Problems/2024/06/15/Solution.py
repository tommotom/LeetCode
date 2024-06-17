class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        can = []
        line = []
        for p, c in zip(profits, capital):
            if c <= w:
                heapq.heappush(can, (-p, c))
            else:
                heapq.heappush(line, (c, p))

        for _ in range(k):
            if not can: break
            pj = heapq.heappop(can)
            w -= pj[0]
            while line and line[0][0] <= w:
                pj = heapq.heappop(line)
                heapq.heappush(can, (-pj[1], pj[0]))

        return w
