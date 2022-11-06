class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if 2 * candidates >= len(costs):
            return sum(sorted(costs)[:k])

        q = []
        for i in range(candidates):
            heapq.heappush(q, (costs[i], 0))
            heapq.heappush(q, (costs[len(costs)-i-1], 1))

        ans, l, r = [], candidates, len(costs)-candidates-1
        while l <= r and len(ans) < k:
            c, f = heapq.heappop(q)
            ans.append(c)
            if f == 0:
                heapq.heappush(q, (costs[l], 0))
                l += 1
            else:
                heapq.heappush(q, (costs[r], 1))
                r -= 1

        while len(ans) < k:
            ans.append(heapq.heappop(q)[0])

        return sum(ans)
