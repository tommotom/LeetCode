class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def sum_of_digits(num):
            ret = 0
            while num > 0:
                ret += num % 10
                num //= 10
            return ret

        def is_beautiful(num):
            return sum_of_digits(num) <= target

        d = 10
        ans = 0
        while not is_beautiful(n):
            num = (n % d) // (d//10)
            ans += d - num * (d//10)
            n += d - num * (d//10)
            d *= 10

        return ans
