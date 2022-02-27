class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def trips(m):
            ret = 0
            for t in time:
                ret += m // t
            return ret

        l, r = 0, 10**15
        while l < r:
            m = l + (r - l) // 2
            if trips(m) < totalTrips:
                l = m + 1
            else:
                r = m
        return l
