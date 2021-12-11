class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(a, b):
            if a == 0: return b
            return gcd(b%a, a)

        c = a // gcd(a, b) * b

        l, r = 0, n * min(a, b)

        while l < r:
            m = (l+r) // 2
            if m // a + m // b - m // c < n:
                l = m + 1
            else:
                r = m

        return l % (10**9 + 7)
