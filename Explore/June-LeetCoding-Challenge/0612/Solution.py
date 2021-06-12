class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.sort()
        q = []
        fuel = startFuel
        i = 0
        mile = 0
        ans = 0
        while fuel > 0 and mile < target:
            mile += fuel
            fuel = 0
            while i < len(stations) and stations[i][0] <= mile:
                heapq.heappush(q, -stations[i][1])
                i += 1
            if q and mile < target:
                fuel -= heapq.heappop(q)
                ans += 1
        if mile < target:
            return -1
        return ans
