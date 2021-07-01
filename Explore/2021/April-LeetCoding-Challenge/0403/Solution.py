class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        idx = {}
        level = 0
        ans = 0
        for i, c in enumerate(s):
            if c == "(":
                if level not in idx:
                    idx[level] = i
                level += 1
            else:
                if level in idx:
                    del idx[level]
                level -= 1
                if level in idx:
                    ans = max(ans, i-idx[level]+1)
        return ans
