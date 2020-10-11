class Solution:
    def maxDepth(self, s: str) -> int:
        nest = ans = 0
        for char in s:
            if char == "(":
                nest += 1
                ans = max(ans, nest)
            elif char == ")":
                nest -= 1

        return ans
