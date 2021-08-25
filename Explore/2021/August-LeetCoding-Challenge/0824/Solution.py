class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        def parseReal(num):
            for i in range(len(num)):
                if num[i] == "+": return int(num[:i])

        def parseImaginary(num):
            for i in range(len(num)):
                if num[i] == "+": return int(num[i+1:-1])

        real1, imaginary1 = parseReal(num1), parseImaginary(num1)
        real2, imaginary2 = parseReal(num2), parseImaginary(num2)

        ret_real = str(real1*real2 + (-1) * imaginary1 * imaginary2)
        ret_imaginary = str(real1*imaginary2 + real2*imaginary1)
        return ret_real + "+" + ret_imaginary + "i"
