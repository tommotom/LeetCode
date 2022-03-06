class Solution:
    MOD = 10 ** 9 + 7

    @cache
    def countOrders(self, n: int) -> int:
        if n == 1: return 1
        intervals = 2*(n-1) + 1
        return (self.countOrders(n-1) * ((intervals) * (intervals+1) // 2 % self.MOD)) % self.MOD
