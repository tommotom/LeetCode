class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        str_num = list(num)
        while len(str_num) > 0 and str_num[-1] == "0":
            str_num.pop()
        return "".join(str_num)
