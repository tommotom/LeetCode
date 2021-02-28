class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ans = float('inf')

        for base in baseCosts:
            can = [base]
            for topping in toppingCosts:
                tmp = []
                for c in can:
                    tmp.append(c + topping)
                    tmp.append(c + topping + topping)
                for t in tmp:
                    can.append(t)

            for c in can:
                if abs(ans - target) > abs(c - target): ans = c
                elif abs(ans - target) == abs(c - target): ans = min(ans, c)

        return ans
