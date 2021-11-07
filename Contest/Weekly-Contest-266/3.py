class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def isValid(m):
            tmp = 0
            for q in quantities:
                tmp += math.ceil(q/m)
            return tmp <= n

        l, r = 1, sum(quantities)+1
        while l < r:
            m = (l + r) // 2
            if isValid(m):
                r = m
            else:
                l = m+1
        return l
