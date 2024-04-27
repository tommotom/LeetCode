class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        q = [(0, 0, 0)]
        shortest = {}
        while q:
            step, k, r = heapq.heappop(q)
            if -k == len(key):
                return step
            if (k, r) in shortest and step >= shortest[(k, r)]: continue
            shortest[(k, r)] = step
            if key[-k] == ring[r]:
                heapq.heappush(q, (step+1, k-1, r))
            else:
                heapq.heappush(q, (step+1, k, 0 if r == len(ring)-1 else r+1))
                heapq.heappush(q, (step+1, k, len(ring)-1 if r == 0 else r-1))
