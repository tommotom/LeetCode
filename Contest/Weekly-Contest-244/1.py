class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]: break
            else:
                continue
            break
        else:
            return True
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[j][n-i-1]: break
            else:
                continue
            break
        else:
            return True
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n-i-1][n-j-1]: break
            else:
                continue
            break
        else:
            return True
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n-j-1][i]: break
            else:
                continue
            break
        else:
            return True
        return False