class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows * cols != r * c: return mat

        ans = []
        i = j = 0
        for _ in range(r):
            row = []
            for __ in range(c):
                row.append(mat[i][j])
                if j+1 == cols:
                    i += 1
                    j = 0
                else:
                    j += 1
            ans.append(row)

        return ans
