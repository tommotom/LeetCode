class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        t_count = Counter(target)
        s_count = Counter(s)
        ans = []
        for k, v in t_count.items():
            if k not in s_count:
                ans.append(0)
            else:
                ans.append(s_count[k] // v)
        return min(ans)
