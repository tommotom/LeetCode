class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0

        def helper(n, row, queens_at):
            nonlocal ans
            if row == n:
                ans += 1
                return
            for col in range(n):
                if isValid(row, col, queens_at):
                    queens_at.append((row, col))
                    helper(n, row+1, queens_at)
                    queens_at.pop()

        def isValid(row, col, queens_at):
            for r, c in queens_at:
                if c == col: return False
                elif row - abs(col - c) == r: return False
            return True

        helper(n, 0, [])
        return ans
