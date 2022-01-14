class Solution:
    def myAtoi(self, s: str) -> int:
        upper, lower = pow(2, 31) - 1, pow(2,31)

        s = s.strip()
        if not s: return 0

        i = 0
        sign = 1
        if s and s[i] == "+" or s[i] == "-":
            sign = int(s[i] + "1")
            i += 1

        num = 0
        while i < len(s):
            if not s[i].isdigit():
                break

            num = num * 10 + int(s[i])
            i += 1

            if sign > 0 and num >= upper:
                return upper
            if sign < 0 and num >= lower:
                return -lower

        return sign * num
