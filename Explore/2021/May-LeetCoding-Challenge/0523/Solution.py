class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        shared = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: continue
                w1, w2 = words[i], words[j]
                for l in range(min(len(w1), len(w2))):
                    if w1[len(w1)-l:] == w2[:l]:
                        shared[i][j] = l

        dp = [[""]*n for _ in range(1<<n)]

        for i in range(1<<n):
            for j in range(n):
                if not i & (1<<j):
                    continue
                if i == (1<<j):
                    dp[i][j] = words[j]
                for k in range(n):
                    if j == k:
                        continue
                    if i & (1<<k):
                        s = dp[i ^ (1<<j)][k]
                        s += words[j][shared[k][j]:]
                        if dp[i][j] == "" or len(s) < len(dp[i][j]):
                            dp[i][j] = s

        minLen = float("inf")
        ans = ""
        for j in range(n):
            if len(dp[(1<<n)-1][j]) < minLen:
                minLen = len(dp[-1][j])
                ans = dp[-1][j]
        return ans
