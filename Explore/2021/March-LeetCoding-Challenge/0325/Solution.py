class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        M, N = len(matrix), len(matrix[0])

        canFlowPacific = [[False] * N for _ in range(M)]
        stack = []
        for i in range(M):
            canFlowPacific[i][0] = True
            stack.append((i, 0))
        for j in range(N):
            canFlowPacific[0][j] = True
            stack.append((0, j))

        while stack:
            m, n = stack.pop()
            if m > 0 and not canFlowPacific[m-1][n] and matrix[m-1][n] >= matrix[m][n]:
                canFlowPacific[m-1][n] = True
                stack.append((m-1, n))
            if n > 0 and not canFlowPacific[m][n-1] and matrix[m][n-1] >= matrix[m][n]:
                canFlowPacific[m][n-1] = True
                stack.append((m, n-1))
            if m+1 < M and not canFlowPacific[m+1][n] and matrix[m+1][n] >= matrix[m][n]:
                canFlowPacific[m+1][n] = True
                stack.append((m+1, n))
            if n+1 < N and not canFlowPacific[m][n+1] and matrix[m][n+1] >= matrix[m][n]:
                canFlowPacific[m][n+1] = True
                stack.append((m, n+1))


        canFlowAtlantic = [[False] * N for _ in range(M)]
        stack = []
        for i in range(M):
            canFlowAtlantic[i][N-1] = True
            stack.append((i, N-1))
        for j in range(N):
            canFlowAtlantic[M-1][j] = True
            stack.append((M-1, j))

        while stack:
            m, n = stack.pop()
            if m > 0 and not canFlowAtlantic[m-1][n] and matrix[m-1][n] >= matrix[m][n]:
                canFlowAtlantic[m-1][n] = True
                stack.append((m-1, n))
            if n > 0 and not canFlowAtlantic[m][n-1] and matrix[m][n-1] >= matrix[m][n]:
                canFlowAtlantic[m][n-1] = True
                stack.append((m, n-1))
            if m+1 < M and not canFlowAtlantic[m+1][n] and matrix[m+1][n] >= matrix[m][n]:
                canFlowAtlantic[m+1][n] = True
                stack.append((m+1, n))
            if n+1 < N and not canFlowAtlantic[m][n+1] and matrix[m][n+1] >= matrix[m][n]:
                canFlowAtlantic[m][n+1] = True
                stack.append((m, n+1))

        ans = []

        for i in range(M):
            for j in range(N):
                if canFlowPacific[i][j] and canFlowAtlantic[i][j]: ans.append([i, j])
        return ans
