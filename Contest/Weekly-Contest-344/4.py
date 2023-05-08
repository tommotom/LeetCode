class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        def helper(node):
            nonlocal ans
            if node > n: return 0
            left, right = helper(2*node), helper(2*node+1)
            ans += abs(left - right)
            return max(left, right) + cost[node-1]

        helper(1)

        return ans
