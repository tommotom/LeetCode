class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(dict)
        for u, v, c in edges:
            self.graph[u][v] = c

    def addEdge(self, edge: List[int]) -> None:
        u, v, c = edge
        self.graph[u][v] = c

    def shortestPath(self, node1: int, node2: int) -> int:
        q = [(0, node1)]
        visited = {}
        while q:
            c, u = heapq.heappop(q)
            if u == node2: return c
            if u in visited and visited[u] <= c: continue
            visited[u] = c
            for v in self.graph[u]:
                path = self.graph[u][v]
                if v in visited and c + path >= visited[v]: continue
                heapq.heappush(q, (c + path, v))
        return -1



    # Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
