from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = defaultdict(lambda:0)
        ans = 0
        for t in time:
            surplus = t % 60
            if surplus == 0:
                ans += d[0]
            else:
                ans += d[60-surplus]
            d[surplus] += 1
        return ans
