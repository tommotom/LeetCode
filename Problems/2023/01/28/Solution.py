class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        arr = [value, value]
        i = bisect.bisect_right(self.intervals, arr)
        left = right = False
        if i > 0 and self.intervals[i-1][1] >= value - 1:
            self.intervals[i-1][1] = max(self.intervals[i-1][1], value)
            left = True
        if i < len(self.intervals) and self.intervals[i][0] <= value + 1:
            self.intervals[i][0] = min(self.intervals[i][0], value)
            right = True

        if not left and not right:
            self.intervals.insert(i, arr)
        elif i > 0 and i < len(self.intervals) and self.intervals[i-1][1] == self.intervals[i][0]:
            self.intervals[i-1][1] = max(self.intervals[i-1][1], self.intervals[i][1])
            self.intervals.pop(i)

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
