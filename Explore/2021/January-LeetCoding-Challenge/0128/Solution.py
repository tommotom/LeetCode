class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        arr = []
        for i in range(n):
            quota = k - (n-i-1) * 26
            quota = 1 if quota < 1 else quota
            arr.append(chr(quota + 96))
            k -= quota
        return "".join(arr)
