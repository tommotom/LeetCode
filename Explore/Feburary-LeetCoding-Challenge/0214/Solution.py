from collections import defaultdict
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        edges = defaultdict(list)
        for i in range(n):
            for j in graph[i]:
                edges[i].append(j)

        visited = [False for _ in range(n)]
        colors = [0 for _ in range(n)]

        q = deque()

        for i, edge in enumerate(graph):
            if edge:
                q.append((i, 1))
                break

        while q:
            node, color = q.popleft()
            visited[node] = True

            if colors[node] != 0 and colors[node] != color: return False
            colors[node] = color

            for v in edges[node]:
                if visited[v]:
                    if color == 1 and colors[v] == 1: return False
                    if color == 2 and colors[v] == 2: return False
                    continue
                if color == 1:
                    q.append((v, 2))
                else:
                    q.append((v, 1))

            if not q:
                for i, edge in enumerate(graph):
                    if edge and not visited[i]:
                        q.append((i, 1))
                        break

        return True
