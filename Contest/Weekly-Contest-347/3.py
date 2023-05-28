class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        l, r = 0, n - 1
        left, right = s[l], s[r]
        cost = 0
        while l < r:
            while l < r and s[l+1] == left: l += 1
            while l < r and s[r-1] == right: r -= 1
            if l == r: break
            l_cost, r_cost = l+1, n-r
            if l_cost < r_cost:
                left = "1" if left == "0" else "0"
            else:
                right = "1" if right == "0" else "0"
            cost += min(l_cost, r_cost)
        return cost
