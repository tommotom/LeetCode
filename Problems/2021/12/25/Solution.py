class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = []
        ops = []
        op = set(["+","-","*","/"])
        for c in s:
            if c == " ":
                continue

            if c.isdigit():
                num.append(c)
            else:
                stack.append(int("".join(num)))
                num = []

                if ops:
                    if ops[-1] == "*":
                        ops.pop()
                        tmp = stack.pop()
                        stack[-1] *= tmp
                    elif ops[-1] == "/":
                        ops.pop()
                        tmp = stack.pop()
                        stack[-1] //= tmp

            if c in op:
                ops.append(c)

        stack.append(int("".join(num)))
        if ops:
            if ops[-1] == "*":
                ops.pop()
                tmp = stack.pop()
                stack[-1] *= tmp
            elif ops[-1] == "/":
                ops.pop()
                tmp = stack.pop()
                stack[-1] //= tmp


        n = stack[0]
        for i in range(len(ops)):
            if ops[i] == "+":
                n += stack[i+1]
            else:
                n -= stack[i+1]

        return n
