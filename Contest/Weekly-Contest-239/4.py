class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(reverse=True)
        h = []
        ans = {}
        for q in sorted(queries):
            while intervals and intervals[-1][0] <= q:
                s, e = intervals.pop()
                if s <= q:
                    heapq.heappush(h, [e-s+1, e])
            while h and h[0][1] < q:
                heapq.heappop(h)
            ans[q] = h[0][0] if h else -1
        return [ans[q] for q in queries]
