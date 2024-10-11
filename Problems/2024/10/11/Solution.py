class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        friends = sorted([[times[i][0], times[i][1], i] for i in range(len(times))], key=lambda x: (x[0], x[1]))

        occupied = []
        vacant = []
        seat = -1
        t = 0

        for a, l, i in friends:
            t = max(t, a)
            while occupied and occupied[0][0] <= t:
                _, s = heapq.heappop(occupied)
                heapq.heappush(vacant, s)
            if not vacant:
                seat += 1
                heapq.heappush(vacant, seat)
            sit = heapq.heappop(vacant)
            if i == targetFriend:
                return sit
            heapq.heappush(occupied, (l, sit))

        return -1
