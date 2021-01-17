class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row-1][col]

            curr = sorted(matrix[row], reverse=True)
            for i in range(len(matrix[row])):
                ans = max(ans, curr[i] * (i + 1))
        return ans
