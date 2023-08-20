class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x: x[1])
        ended = [-1]
        money = {-1:0}
        for s, e, m in offers:
            i = bisect.bisect_left(ended, s)
            cur = money[ended[i-1]] + m
            if e == ended[-1]:
                money[e] = max(money[e], cur)
            elif e > ended[-1] and cur > money[ended[-1]]:
                bisect.insort(ended, e)
                money[e] = cur

        return max(money.values())
