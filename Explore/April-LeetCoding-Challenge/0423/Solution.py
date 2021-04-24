class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        zero = one = last_zero = last_one = ans = 0
        cur = "0"
        for b in s:
            if b == "0":
                if cur == "1":
                    ans += min(one, last_zero)
                    last_one = one
                    one = 0
                    cur = "0"
                zero += 1
            else:
                if cur == "0":
                    ans += min(zero, last_one)
                    last_zero = zero
                    zero = 0
                    cur = "1"
                one += 1
        if cur == "1":
            ans += min(one, last_zero)
        else:
            ans += min(zero, last_one)
        return ans
