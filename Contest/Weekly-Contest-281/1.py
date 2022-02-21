class Solution:
    def countEven(self, num: int) -> int:

        ans = 0
        for n in range(1, num+1):
            tmp = 0
            for c in str(n):
                tmp += int(c)
            if tmp % 2 == 0:
                ans += 1
        return ans
