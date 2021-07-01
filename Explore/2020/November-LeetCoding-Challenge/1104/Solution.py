from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]

        pathes = defaultdict(set)
        for edge in edges:
            pathes[edge[0]].add(edge[1])
            pathes[edge[1]].add(edge[0])

        while len(pathes) > 2:
            one_degree = []
            for i, path in pathes.items():
                if len(path) == 1: one_degree.append(i)
            for i in one_degree:
                p = pathes[i].pop()
                pathes[p].remove(i)
                del pathes[i]

        return [i for i in pathes.keys()]
