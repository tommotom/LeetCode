class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        restricted = set(restricted)
        def helper(cur):
            nonlocal graph, visited
            if cur in restricted: return
            if cur in visited: return
            visited.add(cur)
            for next_node in graph[cur]:
                helper(next_node)

        helper(0)
        return len(visited)
