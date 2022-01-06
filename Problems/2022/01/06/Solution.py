class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2]))
        bus = []
        for p, f, t in trips:

            while bus and bus[0][0] <= f:
                capacity += heapq.heappop(bus)[1]

            if capacity < p: return False
            capacity -= p
            heapq.heappush(bus, (t, p))

        return True
