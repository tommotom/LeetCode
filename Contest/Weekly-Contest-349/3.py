class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        minCosts = list(nums)
        ans = sum(minCosts)
        for ope in range(1, len(nums)):
            for i in range(len(nums)):
                minCosts[i] = min(minCosts[i], nums[(i+ope)%len(nums)])
            ans = min(ans, ope * x + sum(minCosts))
        return ans
