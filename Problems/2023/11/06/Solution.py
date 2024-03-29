class SeatManager:

    def __init__(self, n: int):
        self.q = []
        for i in range(n): heapq.heappush(self.q, i+1)

    def reserve(self) -> int:
        return heapq.heappop(self.q)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.q, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
