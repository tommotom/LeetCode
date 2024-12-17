class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def diff(p, t):
            return p / t - ((p + 1) / (t + 1))

        q = []
        for p, t in classes:
            heapq.heappush(q, (diff(p, t), p, t))

        for _ in range(extraStudents):
            __, p, t = heapq.heappop(q)
            p += 1
            t += 1
            heapq.heappush(q, (diff(p, t), p, t))

        return mean([p / t for _, p, t in q])
