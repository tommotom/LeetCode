class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(bool((x & (1 << i)) ^ (y & (1 << i))) for i in range(32))
