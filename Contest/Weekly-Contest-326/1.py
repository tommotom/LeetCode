class Solution:
    def countDigits(self, num: int) -> int:
        str_num = str(num)
        ans = 0
        for s in str_num:
            if num % int(s) == 0:
                ans += 1
        return ans
