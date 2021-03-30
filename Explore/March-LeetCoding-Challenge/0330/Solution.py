class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        dp = []

        for w, h in envelopes:
            index = bisect.bisect_left(dp, h)

            if index < len(dp):
                dp[index] = h
            else:
                dp.append(h)

        return len(dp)
