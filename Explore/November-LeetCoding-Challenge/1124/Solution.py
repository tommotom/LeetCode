class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0

        s = s.replace(" ", "")

        def parseNum():
            nonlocal i, s
            start = i
            while i < len(s) and s[i].isdigit(): i += 1
            return int(s[start:i])

        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                stack.append(parseNum())
            elif s[i] == "*":
                i += 1
                num = parseNum()
                stack.append(stack.pop() * num)
            elif s[i] == "/":
                i += 1
                num = parseNum()
                stack.append(stack.pop() // num)
            else:
                stack.append(s[i])
                i += 1

        ans = stack[0]
        for i in range(1,len(stack),2):
            if stack[i] == "+": ans += stack[i+1]
            else: ans -= stack[i+1]
        return ans
