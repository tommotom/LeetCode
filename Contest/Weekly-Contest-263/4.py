class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        u_to_v = defaultdict(list)
        for u, v in edges:
            u_to_v[u].append(v)
            u_to_v[v].append(u)

        reached = -1
        q = [(0, 1)]
        visited = set()
        visit_count = [0] * (n+1)
        while q:
            elapsed, node = heapq.heappop(q)

            if (elapsed, node) in visited: continue
            visited.add((elapsed, node))

            if visit_count[node] > 3: continue
            visit_count[node] += 1

            if node == n:
                if reached > 0 and elapsed > reached: return elapsed
                reached = elapsed

            for next_node in u_to_v[node]:
                if (elapsed // change) % 2 == 1:
                    elapsed = change * (elapsed // change + 1)
                heapq.heappush(q, (elapsed+time, next_node))
