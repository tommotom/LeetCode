class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        avail = []
        for i in range(n):
            heapq.heappush(avail, i)
        held = [0] * n
        using = []
        t = 0

        for s, e in meetings:
            t = max(t, s)
            while using and using[0][0] <= t:
                heapq.heappush(avail, heapq.heappop(using)[1])
            if len(avail) == 0:
                t = using[0][0]
                while using and using[0][0] <= t:
                    heapq.heappush(avail, heapq.heappop(using)[1])

            room = heapq.heappop(avail)
            held[room] += 1
            heapq.heappush(using, (t + (e - s), room))

        return held.index(max(held))
