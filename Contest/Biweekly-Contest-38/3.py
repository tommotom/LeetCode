class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        def dist(a, b):
            one = False
            for i in range(len(a)):
                if a[i] != b[i]:
                    if one: return False
                    one = True
            return one

        count = 0
        for length in range(1, min(len(s), len(t)) + 1):
            for i in range(len(s) - length + 1):
                for j in range(len(t) - length + 1):
                    if dist(s[i:i+length], t[j:j+length]): count += 1
        return count
