class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        q = []
        ans = 0
        for s, e in intervals:
            heapq.heappush(q, e)
            while q and q[0] < s:
                heapq.heappop(q)
            ans = max(ans, len(q))
        return ans
