class Solution:
    mod = (10 ** 9) + 7

    @lru_cache(None)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if m == startRow or n == startColumn or startRow < 0 or startColumn < 0: return 1
        if maxMove == 0: return 0

        ret = 0
        ret += self.findPaths(m, n, maxMove-1, startRow-1, startColumn)
        ret %= self.mod
        ret += self.findPaths(m, n, maxMove-1, startRow, startColumn-1)
        ret %= self.mod
        ret += self.findPaths(m, n, maxMove-1, startRow+1, startColumn)
        ret %= self.mod
        ret += self.findPaths(m, n, maxMove-1, startRow, startColumn+1)
        ret %= self.mod
        return ret
