from math import gcd

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = gcd(p, q)
        p //= g
        q //= g
        if q % 2 == 0: return 0
        if p % 2 == 0: return 2
        return 1
