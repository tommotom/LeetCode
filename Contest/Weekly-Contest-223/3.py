class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        ans = len(source)

        G = [set() for _ in range(len(source))]
        for i, j in allowedSwaps:
            G[i].add(j)
            G[j].add(i)
        visited = [False for _ in range(len(source))]

        def dfs(i):
            visited[i] = True
            found.append(i)
            for j in G[i]:
                if not visited[j]:
                    dfs(j)

        for i in range(len(source)):
            if visited[i]: continue
            found = []
            dfs(i)
            count1 = collections.Counter(source[j] for j in found)
            count2 = collections.Counter(target[j] for j in found)
            ans -= sum((count1 & count2).values())

        return ans
