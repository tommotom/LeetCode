class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        def isValid(mat):
            for m in mat:
                if sum(m) != 0: return False
            return True

        def flipAt(i, j, mat):
            nonlocal rows, cols
            mat[i][j] = 1 - mat[i][j]
            if i > 0: mat[i-1][j] = 1 - mat[i-1][j]
            if j > 0: mat[i][j-1] = 1 - mat[i][j-1]
            if i+1 < rows: mat[i+1][j] = 1 - mat[i+1][j]
            if j+1 < cols: mat[i][j+1] = 1 - mat[i][j+1]
            return mat

        def hash(mat):
            nonlocal rows, cols
            n = 0
            ret = 0
            for i in range(rows):
                for j in range(cols):
                    ret += mat[i][j] * (10 ** n)
                    n += 1
            return ret

        rows, cols = len(mat), len(mat[0])

        q = deque([(0, mat)])
        visited = set([hash(mat)])

        while q:
            c, arr = q.popleft()
            if isValid(arr): return c
            for i in range(rows):
                for j in range(cols):
                    tmp = flipAt(i, j, copy.deepcopy(arr))
                    s = hash(tmp)
                    if not s in visited:
                        q.append([c+1, tmp])
                        visited.add(s)
        return -1
