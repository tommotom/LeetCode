class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        paths = defaultdict(list)
        cost = {}
        for u, v, cnt in edges:
            paths[u].append(v)
            paths[v].append(u)
            cost[(u, v)] = cnt
            cost[(v, u)] = cnt

        can_reach_with = [-1] * n
        can_reach_with[0] = maxMoves

        q = deque([(0, maxMoves)])
        while q:
            e, moves = q.popleft()
            for next_e in paths[e]:
                if cost[(e, next_e)] <= moves:
                    rest = moves - cost[(e, next_e)] - 1
                    if can_reach_with[next_e] < rest:
                        can_reach_with[next_e] = rest
                        q.append((next_e, rest))

        ans = 0
        visited = set()
        for e in range(n):
            if can_reach_with[e] >= 0:
                ans += 1
                for next_e in paths[e]:
                    key = (min(e, next_e), max(e, next_e))
                    if key in visited: continue
                    if can_reach_with[next_e] >= 0:
                        ans += min(cost[(e, next_e)], can_reach_with[e] + can_reach_with[next_e])
                    else:
                        ans += can_reach_with[e]
                    visited.add(key)
        return ans
