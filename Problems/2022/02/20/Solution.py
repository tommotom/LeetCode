class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = 1
        last = intervals[0][1]
        for interval in intervals[1:]:
            if interval[1] <= last: continue
            ans += 1
            last = max(last, interval[1])
        return ans
