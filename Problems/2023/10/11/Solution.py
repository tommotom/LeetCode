class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        people = sorted([(t, i) for i, t in enumerate(people)])
        bloom, ans, j = [], [], 0
        for t, i in people:
            while j < len(flowers) and flowers[j][0] <= t:
                heapq.heappush(bloom, flowers[j][1])
                j += 1
            while bloom and bloom[0] < t:
                heapq.heappop(bloom)
            ans.append((i, len(bloom)))
        return [b for _, b in sorted(ans)]
