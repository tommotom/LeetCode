class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        cut = [num-1 for num in range(n+1)]

        for i in range(n):
            j = 0
            while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], cut[i-j]+1)
                j += 1

            j = 1
            while i-j+1 >= 0 and i+j < n and s[i-j+1] == s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], cut[i-j+1]+1)
                j += 1

        return cut[-1]
