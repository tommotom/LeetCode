class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def rev(num):
            ret = 0
            while num > 0:
                ret *= 10
                ret += num % 10
                num //= 10
            return ret

        for n in range(0, num+1):
            if n + rev(n) == num:
                return True
        return False
