class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        dp = [[] for _ in range(k+1)]
        dp[0].append((0, 0))

        for s, e, v in events:
            for i in range(k-1, -1, -1):
                if not dp[i]: continue

                l, r = 0, len(dp[i])
                while l < r:
                    m = l + (r - l) // 2
                    if dp[i][m][0] < s:
                        l = m + 1
                    else:
                        r = m
                l -= 1
                if l < 0: continue
                newVal = dp[i][l][1] + v
                if dp[i+1] and dp[i+1][-1][1] >= newVal: continue
                dp[i+1].append((e, newVal))
        return max(max(r[1] for r in row) if row else 0 for row in dp)
