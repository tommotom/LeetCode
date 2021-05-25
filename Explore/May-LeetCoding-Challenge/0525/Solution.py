class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = set(["+", "-", "*", "/"])
        s = []
        for t in tokens:
            if t in operands:
                num2, num1 = s.pop(), s.pop()
                if t == "+":
                    s.append(num1 + num2)
                elif t == "-":
                    s.append(num1 - num2)
                elif t == "*":
                    s.append(num1 * num2)
                elif t == "/":
                    res = abs(num1) // abs(num2)
                    res = -1 * res if (num1 < 0) ^ (num2 < 0) else res
                    s.append(res)
            else:
                s.append(int(t))
        return s.pop()
