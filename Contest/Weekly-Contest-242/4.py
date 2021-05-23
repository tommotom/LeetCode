class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        for i in range(1, len(stones)):
            stones[i] += stones[i-1]

        ans = stones[-1]
        for v in stones[-2:0:-1]:
            ans = max(ans, v-ans)
        return ans
