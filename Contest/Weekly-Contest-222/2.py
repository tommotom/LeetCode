from collections import defaultdict

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        freq = defaultdict(lambda:0)
        for x in deliciousness:
            for k in range(22): ans += freq[2**k - x]
            freq[x] += 1
        return ans % (10**9 + 7)
