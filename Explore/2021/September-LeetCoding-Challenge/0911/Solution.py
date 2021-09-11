class Solution:
    def calculate(self, s: str) -> int:
        bracket = {}
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                bracket[stack.pop()] = i


        operators = set(["+", "-"])
        skip = set([")", " "])
        def helper(start, end):
            nonlocal s, bracket, operators, skip
            ret, ope, num, i = 0, [], [], start
            while i < end:
                if s[i] in skip:
                    i += 1
                    continue

                if s[i] in operators:
                    ope.append(s[i])
                    i += 1
                    continue

                if i in bracket:
                    num = helper(i+1, bracket[i])
                    i = bracket[i] + 1
                else:
                    i, num = parseDigit(i)

                sign = -1 if ope and ope.pop() == "-" else 1

                ret += num * sign

            sign = -1 if ope and ope.pop() == "-" else 1
            return ret * sign

        def parseDigit(start):
            nonlocal s
            idx = start
            while idx < len(s) and s[idx].isdigit():
                idx += 1
            return idx, int(s[start:idx])

        return helper(0, len(s))
