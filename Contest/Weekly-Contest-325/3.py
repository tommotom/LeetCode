class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def isValid(m):
            take = 1
            last = price[0]
            for i in range(1, len(price)):
                if price[i] - last >= m:
                    last = price[i]
                    take += 1
            return take >= k


        l, r = 0, price[-1] - price[0]
        while l < r:
            m = l + (r-l) // 2
            if isValid(m):
                l = m + 1
            else:
                r = m

        return l if isValid(l) else l-1
