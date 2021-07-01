class Solution:
    def isNumber(self, s: str) -> bool:

        def isInteger(s):
            if not s:
                return False
            if s[0] == "+" or s[0] == "-":
                return s[1:].isdecimal()
            else:
                return s.isdecimal()

        def isDecimal(s):
            if not s:
                return False
            if s[0] == "+" or s[0] == "-":
                s = s[1:]
            if not s:
                return False

            if s[0] == ".":
                return s[1:].isdecimal()

            i = 1
            while i < len(s):
                if s[i] == ".":
                    break
                i += 1
            else:
                return False

            if i == len(s) - 1:
                return s[:i].isdecimal()

            return s[:i].isdecimal() and s[i+1:].isdecimal()

        i = 0
        while i < len(s):
            if s[i] == "e" or s[i] == "E":
                break
            i += 1
        else:
            return isInteger(s) or isDecimal(s)
        return (isInteger(s[:i]) or isDecimal(s[:i])) and isInteger(s[i+1:])
