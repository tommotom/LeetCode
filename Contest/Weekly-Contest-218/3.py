class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            b = format(i, 'b')
            ans = ans * (2 ** len(b))
            ans += i
            ans %= 10**9 + 7
        return ans
