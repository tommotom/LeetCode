class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        held = [0] * n
        vacant = [i for i in range(n)]
        used = []
        time = 0
        for s, e in meetings:
            time = max(s, time)
            while len(used) > 0 and used[0][0] <= time:
                heapq.heappush(vacant, heapq.heappop(used)[1])
            if len(vacant) == 0:
                time = used[0][0]
                while len(used) > 0 and used[0][0] == time:
                    heapq.heappush(vacant, heapq.heappop(used)[1])

            room = heapq.heappop(vacant)
            held[room] += 1
            heapq.heappush(used, (time-s+e, room))
        return held.index(max(held))
