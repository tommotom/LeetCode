class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        @lru_cache(None)
        def dp(r, c1, c2):
            if not 0 <= c1 < cols or not 0 <= c2 < cols:
                return -inf

            result = grid[r][c1]
            if not c1 == c2:
                result += grid[r][c2]

            if r+1 < rows:
                result += max(dp(r+1, new_c1, new_c2) for new_c1 in [c1, c1+1, c1-1] for new_c2 in [c2, c2+1, c2-1])
            return result

        return dp(0, 0, cols-1)
