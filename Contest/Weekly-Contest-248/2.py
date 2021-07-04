class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        h = []
        for i in range(len(dist)):
            heapq.heappush(h, dist[i]/speed[i])
        time = 0
        while h and h[0] > time:
            heapq.heappop(h)
            time += 1
        return time
