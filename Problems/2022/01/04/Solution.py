class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        i = 0
        ans = 0
        while n >= pow(2, i):
            ans += (1<<i) ^ ((1 << i) & n)
            i += 1
        return ans
