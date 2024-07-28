class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dist1 = [-1] * (n+1)
        dist2 = [-1] * (n+1)
        dist1[1] = 0

        q = [(1, 1)]

        while q:
            u, freq = q.pop(0)
            t = dist1[u] if freq == 1 else dist2[u]

            if t // change % 2 == 1:
                t = (t // change + 1) * change
            t += time

            for v in graph[u]:
                if dist1[v] == -1:
                    dist1[v] = t
                    q.append((v, 1))
                elif dist2[v] == -1 and dist1[v] != t:
                    if v == n: return t
                    dist2[v] = t
                    q.append((v, 2))

        return 0
