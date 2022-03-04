class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        @lru_cache(None)
        def helper(row, glass):
            if row == 0:
                return poured

            left = helper(row-1, glass-1) if glass > 0 else 0
            right = helper(row-1, glass) if glass < row else 0

            return max(0, (left-1)/2) + max(0, (right-1)/2)

        return min(helper(query_row, query_glass), 1)
