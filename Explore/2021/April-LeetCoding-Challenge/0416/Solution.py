class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        top, length = None, 0
        for c in s:
            if top == c:
                length += 1
            else:
                top = c
                length = 1

            stack.append(c)

            while length == k:
                for _ in range(k):
                    stack.pop()
                top = None
                length = 0
                if stack:
                    for char in stack[::-1]:
                        if top and top != char: break
                        top = char
                        length += 1
                        if length == k: break

        return "".join(stack)
