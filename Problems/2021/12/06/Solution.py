class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(sum(1 for p in position if p % 2 == 0), sum(1 for p in position if p % 2 == 1))
