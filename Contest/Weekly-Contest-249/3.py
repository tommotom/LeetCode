class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7

        valid_cols = []
        def gen_valid_cols(arr, row):
            nonlocal m, valid_cols
            if row == m:
                valid_cols.append([n for n in arr])
                return
            if arr[-1] == 0:
                arr.append(1)
                gen_valid_cols(arr, row+1)
                arr.pop()
                arr.append(2)
                gen_valid_cols(arr, row+1)
                arr.pop()
            elif arr[-1] == 1:
                arr.append(0)
                gen_valid_cols(arr, row+1)
                arr.pop()
                arr.append(2)
                gen_valid_cols(arr, row+1)
                arr.pop()
            else:
                arr.append(0)
                gen_valid_cols(arr, row+1)
                arr.pop()
                arr.append(1)
                gen_valid_cols(arr, row+1)
                arr.pop()
        gen_valid_cols([0], 1)
        gen_valid_cols([1], 1)
        gen_valid_cols([2], 1)
        if n == 1: return len(valid_cols)

        @lru_cache(None)
        def is_valid_adj(i, j):
            nonlocal m, valid_cols
            for r in range(m):
                if valid_cols[i][r] == valid_cols[j][r]:
                    return False
            return True

        dp = [[0] * len(valid_cols) for _ in range(n)]
        for i in range(n):
            for j in range(len(valid_cols)):
                if i == 0:
                    dp[i][j] = 1
                else:
                    for k in range(len(valid_cols)):
                        if is_valid_adj(j, k):
                            dp[i][j] = (dp[i][j] + dp[i-1][k]) % mod
        return sum(dp[-1]) % mod
