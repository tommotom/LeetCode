class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        total = pow(2, p) - 1
        mod = 10**9 + 7
        return pow((pow(2, p) - 2), total//2, mod) * (pow(2, p)-1) % mod
