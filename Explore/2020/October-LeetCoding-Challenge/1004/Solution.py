class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2: return intervals

        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        last, ans = intervals[0][1], 1
        for i in intervals[1:]:
            if i[1] <= last: continue
            ans += 1
            last = max(last, i[1])
        return ans
