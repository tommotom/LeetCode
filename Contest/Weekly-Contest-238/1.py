class Solution:
    def sumBase(self, n: int, k: int) -> int:
        m = 0
        while k ** m <= n: m += 1
        m -= 1

        ans = 0
        while n > 0:
            tmp = n // (k ** m)
            n -= (k ** m) * tmp
            ans += tmp
            m -= 1

        return ans
