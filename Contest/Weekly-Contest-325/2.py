class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counter = Counter(s)
        def isOk():
            nonlocal counter
            return counter['a'] >= k and counter['b'] >= k and counter['c'] >= k

        if not isOk(): return -1
        if k == 0: return 0

        l, r = len(s), len(s)
        ans = len(s)
        while l >= 0 and l <= r:
            if isOk():
                ans = min(ans, (l) + (len(s)-r))
                l -= 1
                counter[s[l]] -= 1
            else:
                r -= 1
                counter[s[r]] += 1

        return ans
