class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        q = list()

        ans = 0
        for i in range(len(apples)):
            if apples == 0: continue
            heapq.heappush(q, (i+days[i], apples[i]))
            while q and (q[0][0] <= i or q[0][1] == 0): heapq.heappop(q)
            if q and q[0][1] > 0:
                ans += 1
                item = heapq.heappop(q)
                heapq.heappush(q, (item[0], item[1]-1))

        i = len(apples)
        while q:
            while q and (q[0][0] <= i or q[0][1] == 0): heapq.heappop(q)
            if q and q[0][1] > 0:
                ans += 1
                item = heapq.heappop(q)
                heapq.heappush(q, (item[0], item[1]-1))
            i += 1

        return ans
