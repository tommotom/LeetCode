class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i in range(len(colors)-1):
            for j in range(i+1, len(colors)):
                if colors[i] != colors[j]:
                    ans = max(ans, j - i)
        return ans
