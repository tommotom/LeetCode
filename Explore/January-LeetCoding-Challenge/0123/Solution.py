class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        row, col = 0, n
        while col > 0 or row < m:
            tmp = []
            i, j = row, col
            while i < m and j < n:
                tmp.append(mat[i][j])
                i += 1
                j += 1

            tmp.sort()

            i, j, idx = row, col, 0
            while i < m and j < n:
                mat[i][j] = tmp[idx]
                i += 1
                j += 1
                idx += 1

            if col > 0: col -= 1
            else: row += 1

        return mat
