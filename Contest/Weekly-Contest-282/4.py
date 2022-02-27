class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        go_straight = [float('inf') for _ in range(20)]
        go_straight[0] = 0
        for i in range(1, 20):
            for f, r in tires:
                cost = (f*pow(r,i)-f)//(r-1)
                go_straight[i] = min(go_straight[i], cost)
            if go_straight[i] > 2 * 10**5: break

        dp = [float('inf') for _ in range(numLaps+1)]
        for i in range(min(len(dp), len(go_straight))):
            dp[i] = go_straight[i]

        for i in range(1, len(dp)):
            for j in range(1, i):
                dp[i] = min(dp[i], dp[i-j] + changeTime + dp[j])

        return dp[-1]
