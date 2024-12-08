class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: (x[0], x[1]))
        q = []
        ans = max_ever = 0
        for s, e, v in events:
            while q and q[0][0] < s:
                max_ever = max(max_ever, heapq.heappop(q)[1])
            ans = max(ans, max_ever + v)
            heapq.heappush(q, (e, v))

        return ans
