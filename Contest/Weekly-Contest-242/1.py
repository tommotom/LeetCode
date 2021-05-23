class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        o_c = z_c = o = z = 0
        for c in s:
            if c == "1":
                z_c = 0
                o_c += 1
            else:
                z_c += 1
                o_c = 0
            o = max(o, o_c)
            z = max(z, z_c)
        return o > z