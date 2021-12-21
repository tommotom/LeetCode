class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        return Counter(bin(n))["1"] <= 1
