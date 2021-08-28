class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[1])
        dp = [[0,0]]
        for start, end, pro in jobs:
            i = bisect.bisect(dp, [start+1])-1
            if dp[i][1] + pro > dp[-1][1]:
                dp.append([end, dp[i][1] + pro])
        return dp[-1][1]
