class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)

        if rows == 0: return 0

        cols = len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            acc = 0
            for j in range(cols):
                if matrix[i][j] == "1":
                    acc += 1
                else:
                    acc = 0
                dp[i][j] = acc

        ret = 0
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                bottom, right = dp[i][j], 0

                k = i
                while k > -1 and dp[k][j]:
                    bottom = min(bottom, dp[k][j])
                    right += 1

                    ret = max(ret, bottom * right)
                    k -= 1
        return ret
