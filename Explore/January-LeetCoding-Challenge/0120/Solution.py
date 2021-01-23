class Solution:
    def isValid(self, s: str) -> bool:
        begin = set(["(", "[", "{"])
        stack = []
        for c in s:
            if c in begin:
                stack.append(c)
                continue

            if not stack: return False

            paren = stack.pop()

            if c == ")" and not paren == "(": return False
            if c == "]" and not paren == "[": return False
            if c == "}" and not paren == "{": return False

        if stack: return False

        return True
