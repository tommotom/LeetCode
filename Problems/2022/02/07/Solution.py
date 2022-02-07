class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_c, t_c = Counter(s), Counter(t)
        for k in t_c:
            if not k in s_c or t_c[k] > s_c[k]: return k
        return ""
