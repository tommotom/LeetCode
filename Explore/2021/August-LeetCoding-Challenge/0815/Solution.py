class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = defaultdict(int)
        target = Counter(t)

        def isInclude():
            nonlocal counter, target
            for k, v in target.items():
                if counter[k] < v: return False
            return True

        l = r = 0
        counter[s[0]] += 1
        ans = ""
        while True:
            while r+1 < len(s) and not isInclude():
                r += 1
                counter[s[r]] += 1

            if r == len(s)-1 and not isInclude():break

            while l <= r:
                if isInclude() and (ans == "" or len(ans) > r - l + 1):
                    ans = s[l:r+1]
                counter[s[l]] -= 1
                l += 1
                if not isInclude():
                    break
        return ans