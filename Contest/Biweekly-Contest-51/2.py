class SeatManager:

    def __init__(self, n: int):
        self.seats = []
        for i in range(1, n+1):
            heapq.heappush(self.seats, i)

    def reserve(self) -> int:
        if len(self.seats) == 0: return
        return heapq.heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
