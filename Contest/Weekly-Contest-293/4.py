class CountIntervals:

    def __init__(self):
        self.intervals = []
        self.ans = 0

    def add(self, left: int, right: int) -> None:
        l, r = 0, len(self.intervals)
        while l < r:
            m = l + (r - l) // 2
            if self.intervals[m][0] < left:
                l = m + 1
            else:
                r = m

        if self.canMergeWithLeft(left, l):
            self.ans += max(right - self.intervals[l-1][1], 0)
            self.intervals[l-1][1] = max(right, self.intervals[l-1][1])
            l -= 1
        else:
            bisect.insort(self.intervals, [left, right])
            self.ans += right - left + 1

        while self.canMergeWithRight(l):
            self.ans -= min(self.intervals[l+1][1], self.intervals[l][1]) - self.intervals[l+1][0] + 1
            self.intervals[l][1] = max(self.intervals[l][1], self.intervals[l+1][1])
            self.intervals.pop(l+1)

    def canMergeWithLeft(self, left, i):
        if i == 0: return False
        return self.intervals[i-1][1] >= left

    def canMergeWithRight(self, i):
        if not i+1 < len(self.intervals): return False
        return self.intervals[i][1] >= self.intervals[i+1][0]


    def count(self) -> int:
        return self.ans


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
