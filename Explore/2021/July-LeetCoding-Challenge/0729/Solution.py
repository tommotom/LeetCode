class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        ans = [[float('inf')] * n for _ in range(m)]
        q = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))

        while q:
            i, j, dist = q.popleft()
            ans[i][j] = min(ans[i][j], dist)

            if i > 0 and ans[i-1][j] > dist+1:
                q.append((i-1, j, dist+1))
            if j > 0 and ans[i][j-1] > dist+1:
                q.append((i, j-1, dist+1))
            if i+1 < m and ans[i+1][j] > dist+1:
                q.append((i+1, j, dist+1))
            if j+1 < n and ans[i][j+1] > dist+1:
                q.append((i, j+1, dist+1))
        return ans
