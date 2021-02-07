class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        while i < len(path):
            if path[i] == "/": i += 1
            else:
                j = i
                while j+1 < len(path) and path[j+1] != "/": j += 1
                tmp = path[i:j+1]
                if tmp == ".": pass
                elif tmp == "..":
                    if stack: stack.pop()
                else:
                    stack.append(tmp)
                i = j+1

        return "/" + "/".join(stack)
