class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, pow(10, 9)
        while l < r:
            k = l + (r-l) // 2
            hour = 0
            for p in piles:
                hour += math.ceil(p/k)
            if hour > h:
                l = k + 1
            else:
                r = k
        return l
