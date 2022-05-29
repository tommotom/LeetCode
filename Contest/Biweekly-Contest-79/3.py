class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = [0] * n
        for a, b in roads:
            count[a] += 1
            count[b] += 1
        count.sort()
        ans = 0
        for i in range(n):
            ans += count[i] * (i+1)
        return ans
