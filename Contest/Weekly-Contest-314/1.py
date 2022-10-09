class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        logs = [[0,0]] + logs
        ans = 0
        time = 0
        for i in range(1, len(logs)):
            t = logs[i][1] - logs[i-1][1]
            if time < t:
                time = t
                ans = logs[i][0]
            elif time == t:
                ans = min(ans, logs[i][0])

        return ans
