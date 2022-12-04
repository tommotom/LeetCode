class UF:
    def __init__(self, n):
        self.ids = [i for i in range(n)]
        self.m = [float('inf') for _ in range(n)]

    def find(self, u):
        if u == self.ids[u]: return u
        v = self.find(self.ids[u])
        self.ids[u] = v
        return v

    def union(self, u, v, score):
        u = self.find(u)
        v = self.find(v)
        score = min([score, self.m[u], self.m[v]])
        self.m[u] = self.m[v] = score
        self.ids[u] = v

    def score(self, u):
        if u == self.ids[u]: return self.m[u]
        return min(self.m[u], self.m[self.find(u)])

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UF(n)
        for u, v, s in roads:
            uf.union(u-1, v-1, s)
        return uf.score(0)
