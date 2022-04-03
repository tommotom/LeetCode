class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def isValid(num):
            pile = 0
            for can in candies:
                pile += can // num
            return pile >= k

        l, r = 1, max(candies)
        while l < r:
            m = l + (r - l) // 2
            if isValid(m):
                l = m + 1
            else:
                r = m
        return l if isValid(l) else l - 1
