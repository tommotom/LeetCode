from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacent = defaultdict(list)
        for p1, p2 in adjacentPairs:
            adjacent[p1].append(p2)
            adjacent[p2].append(p1)

        for k, v in adjacent.items():
            if len(v) == 1:
                key = k
                break

        ans = []
        visited = set()
        while True:
            ans.append(key)
            visited.add(key)
            for k in adjacent[key]:
                if k in visited: continue
                key = k
                break
            else:
                break
        return ans
