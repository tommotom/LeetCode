class StockPrice:

    def __init__(self):
        self.maxs = []
        self.mins = []
        self.curs = []
        self.vals = {}

    def update(self, timestamp: int, price: int) -> None:
        self.vals[timestamp] = price
        heapq.heappush(self.maxs, (-price, timestamp))
        heapq.heappush(self.mins, (price, timestamp))
        heapq.heappush(self.curs, (-timestamp, price))

    def current(self) -> int:
        t, p = -self.curs[0][0], self.curs[0][1]
        while self.vals[t] != p:
            heapq.heappop(self.curs)
            t, p = -self.curs[0][0], self.curs[0][1]
        return p

    def maximum(self) -> int:
        p, t = -self.maxs[0][0], self.maxs[0][1]
        while self.vals[t] != p:
            heapq.heappop(self.maxs)
            p, t = -self.maxs[0][0], self.maxs[0][1]
        return p

    def minimum(self) -> int:
        p, t = self.mins[0]
        while self.vals[t] != p:
            heapq.heappop(self.mins)
            p, t = self.mins[0]
        return p

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
