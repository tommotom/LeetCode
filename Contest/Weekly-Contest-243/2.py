class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == "-":
            i = 1
            while i < len(n) and int(n[i]) <= x:
                i += 1
            return n[:i]+str(x)+n[i:]
        else:
            i = 0
            while i < len(n) and int(n[i]) >= x:
                i += 1
            return n[:i]+str(x)+n[i:]
