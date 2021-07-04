class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def myPow(a, b, m):
            if b == 0: return 1
            if b % 2 == 0:
                return myPow(a*a%m, b//2, m)
            return a * myPow(a, b-1, m)

        mod = 10 ** 9 + 7
        if n == 1: return 5
        odd = n // 2
        even = n - odd

        return myPow(5, even, mod) * myPow(4, odd, mod) % mod
