class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        until = []
        ans = 1
        for l, r in intervals:
            while until and until[0] < l: heapq.heappop(until)
            heapq.heappush(until, r)
            ans = max(ans, len(until))
        return ans
