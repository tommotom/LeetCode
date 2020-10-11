from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connected = defaultdict(set)
        for road in roads:
            connected[road[0]].add(tuple(road))
            connected[road[1]].add(tuple(road))

        ans = 0
        for i in range(n-1):
            for j in range(i, n):
                ans = max(ans, len(connected[i] | connected[j]))
        return ans
