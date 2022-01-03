class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = Counter([t % 60 for t in time])
        ans = 0
        if 0 in counter:
            ans += counter[0] * (counter[0] - 1) // 2
        if 30 in counter:
            ans += counter[30] * (counter[30] - 1) // 2
        for key, value in counter.items():
            if key >= 30: continue
            if 60 - key in counter:
                ans += counter[key] * counter[60 - key]
        return ans
