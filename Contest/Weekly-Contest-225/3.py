class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        values = []
        for i in range(len(matrix)):
            row = None
            for j in range(len(matrix[0])):
                if row:
                    tmp = matrix[i][j]
                    matrix[i][j] ^= row
                    row ^= tmp
                else: row = matrix[i][j]
                if i > 0: matrix[i][j] ^= matrix[i-1][j]
                values.append(matrix[i][j])
        return sorted(values, reverse=True)[k-1]
