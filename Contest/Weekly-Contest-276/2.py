class Solution:
    @lru_cache(None)
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target == 1:
            return 0
        if maxDoubles > 0 and target % 2 == 0:
            return self.minMoves(target//2, maxDoubles-1) + 1
        if maxDoubles == 0:
            return target - 1
        return self.minMoves(target-1, maxDoubles) + 1
