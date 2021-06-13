class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isValid(i):
            nonlocal s, p, removable

            rem = set(removable[:i+1])

            i = j = 0
            while i < len(s) and j < len(p):
                if i in rem:
                    i += 1
                    continue
                if s[i] != p[j]:
                    i += 1
                else:
                    i += 1
                    j += 1
            return j == len(p)

        l, r = 0, len(removable)+1
        while l < r:
            m = (l + r) // 2
            if isValid(m):
                l = m + 1
            else:
                r = m
        return l if l < len(removable) else l-1

