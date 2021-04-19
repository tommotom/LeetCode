class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i, n = 0, len(costs)
        while i < n and costs[i] <= coins:
            coins -= costs[i]
            i += 1
        return i
