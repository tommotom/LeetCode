class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def horizontal(r, c):
            nonlocal board, word, rows, cols
            if not (c == 0 or board[r][c-1] == "#"): return False
            if not (c+len(word) == cols or (c+len(word) < cols and board[r][c+len(word)] == "#")): return False
            for i, w in enumerate(word):
                if not (board[r][c+i] == " " or board[r][c+i] == w): break
            else:
                return True
            for i, w in enumerate(word[::-1]):
                if not (board[r][c+i] == " " or board[r][c+i] == w): break
            else:
                return True
            return False

        def vertical(r, c):
            nonlocal board, word, rows, cols
            if not (r == 0 or board[r-1][c] == "#"): return False
            if not (r+len(word) == rows or (r+len(word) < rows and board[r+len(word)][c] == "#")): return False
            for i, w in enumerate(word):
                if not (board[r+i][c] == " " or board[r+i][c] == w): break
            else:
                return True
            for i, w in enumerate(word[::-1]):
                if not (board[r+i][c] == " " or board[r+i][c] == w): break
            else:
                return True
            return False

        for r in range(rows):
            for c in range(cols):
                if horizontal(r, c) or vertical(r, c): return True
        return False
