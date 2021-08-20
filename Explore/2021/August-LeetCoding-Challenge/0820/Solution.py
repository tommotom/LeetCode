class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [[set() for __ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue

                if board[i][j] in rows[i]: return False
                if board[i][j] in cols[j]: return False
                if board[i][j] in blocks[i//3][j//3]: return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                blocks[i//3][j//3].add(board[i][j])

        return True
