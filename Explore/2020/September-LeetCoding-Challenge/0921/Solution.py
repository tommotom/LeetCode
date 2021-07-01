import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        h = []
        passenger = 0
        for trip in trips:
            while h and h[0][0] <= trip[1]:
                passenger -= h[0][1]
                heapq.heappop(h)

            passenger += trip[0]
            heapq.heappush(h, (trip[2], trip[0]))
            if passenger > capacity: return False

        return True
