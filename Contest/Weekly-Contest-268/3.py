class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.indices = defaultdict(list)
        for i, a in enumerate(arr):
            self.indices[a].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        arr = self.indices[value]
        return bisect.bisect(arr, right) - bisect.bisect(arr, left-1)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
