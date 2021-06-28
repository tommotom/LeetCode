class Solution:
    def removeDuplicates(self, s: str) -> str:
        n = len(s)
        ok = [s[0]]
        for j in range(1, n):
            if ok and ok[-1] == s[j]:
                ok.pop()
            else:
                ok.append(s[j])
        return "".join(ok)
