class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        def doa(string):
            ret = ""
            for i in range(len(s)):
                if i % 2 == 0: ret += string[i]
                else: ret += str(int(string[i]) + a)[-1]
            return ret

        def dob(string):
            return (string + string)[len(string)-b:2*len(string)-b]

        def helper(string):
            nonlocal visited
            if string in visited: return
            visited.add(string)
            helper(doa(string))
            helper(dob(string))

        helper(s)
        if not visited: return ""
        return min(visited)
