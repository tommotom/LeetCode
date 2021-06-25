class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edge_count = defaultdict(int)
        ver_to_ver = defaultdict(list)
        for v, w in edges:
            edge_count[v] += 1
            edge_count[w] += 1
            ver_to_ver[v].append(w)
            ver_to_ver[w].append(v)

        q = deque([])
        for v, c in edge_count.items():
            if c == 1: q.append(v)
        if not q: return edges[-1]

        necessary = set()
        while q:
            v = q.popleft()
            for w in ver_to_ver[v]:
                if w > v:
                    necessary.add((v, w))
                else:
                    necessary.add((w, v))
                edge_count[w] -= 1
                if edge_count[w] == 1:
                    q.append(w)
        for edge in reversed(edges):
            if tuple(edge) not in necessary:
                return edge
