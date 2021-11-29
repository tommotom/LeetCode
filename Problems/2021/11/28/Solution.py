class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []

        def helper(i, path):
            nonlocal ans

            if i == n-1:
                ans.append(list(path))
                return

            for g in graph[i]:
                path.append(g)
                helper(g, path)
                path.pop()

        helper(0, [0])

        return ans
