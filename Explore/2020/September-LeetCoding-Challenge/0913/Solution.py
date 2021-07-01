class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals)
        while l < r:
            m = (l + r) // 2
            if intervals[m][0] < newInterval[0]:
                l = m + 1
            else:
                r = m
        lower = l

        l, r = 0, len(intervals)
        while l < r:
            m = (l + r) // 2
            if intervals[m][1] < newInterval[1]:
                l = m + 1
            else:
                r = m
        upper = l

        merge_left = lower > 0 and newInterval[0] <= intervals[lower-1][1]
        merge_right = upper < len(intervals) and intervals[upper][0] <= newInterval[1]

        if merge_left:
            newInterval[0] = intervals[lower-1][0]
            lower -= 1
        if merge_right:
            newInterval[1] = intervals[upper][1]
            upper += 1

        return intervals[:lower] + [newInterval] + intervals[upper:]
