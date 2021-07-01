class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        if not S: return 0
        if S[1] == ")": return 1 + self.scoreOfParentheses(S[2:])
        depth = i = 1
        while depth > 0 and i < len(S):
            if S[i] == "(":
                depth += 1
            else:
                depth -= 1
            i += 1
        return self.scoreOfParentheses(S[1:i-1]) * 2 + self.scoreOfParentheses(S[i:])
