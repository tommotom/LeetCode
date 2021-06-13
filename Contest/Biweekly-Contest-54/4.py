class Solution:
    def minOperationsToFlip(self, e: str) -> int:
        t = {"|": lambda x, y:x|y, "&": lambda x, y:x&y}
        def corr(s):
            stack, d = [], {}
            for i, c in enumerate(e):
                if c == "(":
                    stack.append(i)
                elif c == ")":
                    d[i] = stack.pop()
            return d

        def dfs(beg, end):
            if beg == end: return (int(e[beg]), 1)
            beg2 = d.get(end, end)
            if beg == beg2: return dfs(beg+1, end-1)
            p1, c1 = dfs(beg, beg2-2)
            p2, c2 = dfs(beg2, end)
            op = e[beg2-1]

            c3 = 1 if p1 + p2 == 1 else min(c1, c2) + (p1^(op == "&"))
            return (t[op](p1, p2), c3)

        d = corr(e)
        return dfs(0, len(e)-1)[1]
