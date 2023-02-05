class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1, count2 = Counter(basket1), Counter(basket2)

        whole = count1 + count2
        diff = {}
        for k, v in whole.items():
            if v % 2 == 1: return -1
            diff[k] = abs(count1[k] - count2[k]) // 2

        swap = []
        for k, v in diff.items():
            for _ in range(v):
                swap.append(k)
        swap.sort()
        swap = swap[:len(swap)//2]

        q = []
        for s in swap:
            heapq.heappush(q, -s)

        m = min(whole.keys())
        while q and -q[0] > m*2:
            heapq.heappop(q)
            heapq.heappush(q, -m)
            heapq.heappush(q, -m)

        return -sum(q)
