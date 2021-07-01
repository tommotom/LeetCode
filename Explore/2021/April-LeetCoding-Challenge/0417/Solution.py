class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(1, cols):
                row[i] += row[i-1]

        ans = 0
        for i in range(cols):
            for j in range(i, cols):
                c = collections.defaultdict(int)
                cur, c[0] = 0, 1
                for k in range(rows):
                    cur += matrix[k][j] - (matrix[k][i-1] if i > 0 else 0)
                    ans += c[cur - target]
                    c[cur] += 1
        return ans
