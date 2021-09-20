class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[None] * 3 for _ in range(3)]

        for i, (r, c) in enumerate(moves):
            mark = "X" if i % 2 == 0 else "O"
            board[r][c] = mark

        def judgeWinner(board):
            for i in range(3):
                if all(mark == "O" for mark in board[i]): return "B"
                if all(mark == "X" for mark in board[i]): return "A"
            for j in range(3):
                if board[0][j] == "O" and board[1][j] == "O" and board[2][j] == "O": return "B"
                if board[0][j] == "X" and board[1][j] == "X" and board[2][j] == "X": return "A"
            if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O": return "B"
            if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X": return "A"
            if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O": return "B"
            if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X": return "A"
            return None

        def isDraw(board):
            for i in range(3):
                for j in range(3):
                    if board[i][j] is None: return "Pending"
            return "Draw"

        return judgeWinner(board) or isDraw(board)
