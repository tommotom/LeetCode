class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_c = Counter(s)
        t_c = Counter(t)
        ans = 0
        for key in set(list(s_c.keys()) + list(t_c.keys())):
            if key not in s_c:
                ans += t_c[key]
            elif key not in t_c:
                ans +=  s_c[key]
            else:
                ans += abs(s_c[key] - t_c[key])
        return ans
