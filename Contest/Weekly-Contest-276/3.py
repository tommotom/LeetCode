class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0 for _ in range(len(questions))]
        ans = 0
        for i in range(len(questions)):
            if i > 0: dp[i] = max(dp[i], dp[i-1])

            point, skip = questions[i]
            ans = max(ans, dp[i] + point)
            if i+skip+1 < len(dp):
                dp[i+skip+1] = max(dp[i+skip+1], dp[i] + point)
        return ans
