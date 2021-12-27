class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        n = 1
        while n <= num:
            if not n & num:
                ans += n
            n <<= 1
        return ans
