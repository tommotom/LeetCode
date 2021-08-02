class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, islandId):
            nonlocal n, grid, islandIds
            islandIds[i][j] = islandId
            size = 1
            if i > 0 and grid[i-1][j] == 1 and islandIds[i-1][j] == -1:
                size += dfs(i-1, j, islandId)
            if j > 0 and grid[i][j-1] == 1 and islandIds[i][j-1] == -1:
                size += dfs(i, j-1, islandId)
            if i+1 < n and grid[i+1][j] == 1 and islandIds[i+1][j] == -1:
                size += dfs(i+1, j, islandId)
            if j+1 < n and grid[i][j+1] == 1 and islandIds[i][j+1] == -1:
                size += dfs(i, j+1, islandId)
            return size

        n = len(grid)
        islandIds = [[-1] * n for _ in range(n)]
        islandSize = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0 or not islandIds[i][j] == -1: continue
                islandId = len(islandSize)
                islandSize.append(dfs(i, j, islandId))

        ret = max(islandSize) if islandSize else 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    tmp = 1
                    merged = set()
                    if i > 0 and islandIds[i-1][j] != -1 and islandIds[i-1][j] not in merged:
                        merged.add(islandIds[i-1][j])
                        tmp += islandSize[islandIds[i-1][j]]
                    if j > 0 and islandIds[i][j-1] != -1 and islandIds[i][j-1] not in merged:
                        merged.add(islandIds[i][j-1])
                        tmp += islandSize[islandIds[i][j-1]]
                    if i+1 < n and islandIds[i+1][j] != -1 and islandIds[i+1][j] not in merged:
                        merged.add(islandIds[i+1][j])
                        tmp += islandSize[islandIds[i+1][j]]
                    if j+1 < n and islandIds[i][j+1] != -1 and islandIds[i][j+1] not in merged:
                        merged.add(islandIds[i][j+1])
                        tmp += islandSize[islandIds[i][j+1]]
                    ret = max(ret, tmp)

        return ret
