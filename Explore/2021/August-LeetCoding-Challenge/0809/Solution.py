class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        def process(num, carry, digit, tmp):
            num += pow(10, digit) * (tmp % 10)
            return num, tmp // 10, digit+1

        num = 0
        i1, i2 = len(num1)-1, len(num2)-1
        carry = 0
        digit = 0

        while i1 >= 0 and i2 >= 0:
            tmp = int(num1[i1]) + int(num2[i2]) + carry
            num, carry, digit = process(num, carry, digit, tmp)
            i1 -= 1
            i2 -= 1

        while i1 >= 0:
            tmp = int(num1[i1]) + carry
            num, carry, digit = process(num, carry, digit, tmp)
            i1 -= 1

        if carry: num += pow(10, digit) * carry

        return str(num)
