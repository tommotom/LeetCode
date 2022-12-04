class UF:
    def __init__(self, n):
        self.ids = [i for i in range(n)]

    def find(self, u):
        if u == self.ids[u]: return u
        v = self.find(self.ids[u])
        self.ids[u] = v
        return v

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        self.ids[u] = v

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        uf = UF(n)
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
            uf.union(u-1, v-1)

        groups = defaultdict(list)
        for i, g in enumerate(uf.ids):
            groups[uf.find(g)].append(i)


        def bfs(start):
            q = deque()
            q.append((start,1))
            layers = defaultdict(int)
            layers[start] = 1
            ans = -1

            while q:
                for _ in range(len(q)):
                    node, layer = q.popleft()
                    if layer > ans:
                        ans = layer
                    for x in graph[node]:
                        if x not in layers:
                            q.append((x, layer+1))
                            layers[x] = layer+1
                        if layers[node] == layers[x]:
                            return -1
            return ans

        ans = 0
        for g, arr in groups.items():
            score = -1
            for i in range(len(arr)):
                score = max(score, bfs(arr[i]))
            if score == -1: return -1
            ans += score

        return ans
