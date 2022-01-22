class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = []
        num = 1
        while pow(num, 2) <= n:
            squares.append(pow(num, 2))
            num += 1
        square_set = set(squares)

        @lru_cache(None)
        def helper(n):
            nonlocal squares, square_set
            if n in square_set: return True

            i = 0
            while i < len(squares) and squares[i] < n:
                if not helper(n-squares[i]): return True
                i += 1
            return False

        return helper(n)
