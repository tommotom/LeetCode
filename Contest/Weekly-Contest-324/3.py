class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        odds = []
        for k, v in graph.items():
            if len(v) % 2 == 1: odds.append(k)

        if len(odds) == 4:
            if odds[1] not in graph[odds[0]] and odds[3] not in graph[odds[2]]: return True
            if odds[2] not in graph[odds[0]] and odds[3] not in graph[odds[1]]: return True
            if odds[3] not in graph[odds[0]] and odds[1] not in graph[odds[2]]: return True

        if len(odds) == 2:
            a, b = odds
            if a not in graph[b]: return True
            for k, v in graph.items():
                if k != a and k!= b and a not in v and b not in v: return True

        if len(odds) == 0: return True

        return False
