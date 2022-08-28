class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowConditions = set(map(tuple, rowConditions))
        colConditions = set(map(tuple, colConditions))
        rowGraph = defaultdict(list)
        rowIn = [0] * (k+1)
        for u, v in rowConditions:
            rowGraph[u].append(v)
            rowIn[v] += 1

        colGraph = defaultdict(list)
        colIn = [0] * (k+1)
        for u, v in colConditions:
            colGraph[u].append(v)
            colIn[v] += 1

        def topSort(graph, inCount):
            ret = []
            queue = deque([i for i in range(1, k+1) if inCount[i] == 0])
            while queue:
                u = queue.popleft()
                ret.append(u)
                for v in graph[u]:
                    inCount[v] -= 1
                    if inCount[v] == 0:
                        queue.append(v)
            return ret

        row = topSort(rowGraph, rowIn)
        col = topSort(colGraph, colIn)
        if len(row) != k or len(col) != k: return []

        ans = [[0] * k for _ in range(k)]

        for i, r in enumerate(row):
            ans[i][col.index(r)] = r
        return ans
