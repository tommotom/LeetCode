class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [[] for node in range(n)]
        deg = [0 for node in range(n)]

        for u, v in edges:
            graph[u].append(v)
            deg[v] += 1

        q = []
        dp = [[0 for j in range(26)] for node in range(n)]
        for i in range(n):
            if deg[i] == 0:
                q.append(i)

        count = 0
        ans = -1
        while q != []:
            cur = q.pop()
            count += 1
            dp[cur][ord(colors[cur])-ord('a')] += 1
            ans = max(ans, dp[cur][ord(colors[cur])-ord('a')])
            for neigh in graph[cur]:
                for i in range(26):
                    dp[neigh][i] = max(dp[neigh][i], dp[cur][i])
                deg[neigh] -= 1
                if deg[neigh] == 0:
                    q.append(neigh)
            if count == n:
                break

        if q != [] or count < n:
            return -1

        return ans
