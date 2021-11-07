class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str_to_int(num):
            ret = 0
            for digit, char in enumerate(num[::-1]):
                ret += (ord(char) - ord('0')) * pow(10, digit)
            return ret

        return str(str_to_int(num1) * str_to_int(num2))
