class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(small) > len(large):
            heapq.heappush(large, -heapq.heappop(small))

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(small) < len(large):
            return float(large[0])
        return (large[0] - small[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
