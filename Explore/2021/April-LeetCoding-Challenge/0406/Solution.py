class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0: return n * n // 4
        return (n+1) * (n-1) // 4
