class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        mul = 1
        while divisor << 1 <= dividend:
            divisor <<= 1
            mul <<= 1

        ans = 0
        while mul >= 1 and dividend >= divisor:
            dividend -= divisor
            ans += mul
            while mul > 1 and dividend < divisor:
                divisor >>= 1
                mul >>= 1

        if not sign and ans > 2 ** 31 -1: ans = 2 ** 31 - 1

        if sign: return -ans
        return ans
