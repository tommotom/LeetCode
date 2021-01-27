class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 1
        modulo = 10 ** 9 + 7
        for num in range(2, n+1):
            b = bin(num)[2:]
            ans = (ans << len(b)) + num
            ans %= modulo
        return ans
