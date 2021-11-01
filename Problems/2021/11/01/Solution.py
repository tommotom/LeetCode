class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(i, j):
            board[i][j] = "OO"
            if i > 0 and board[i-1][j] == "O":
                dfs(i-1, j)
            if j > 0 and board[i][j-1] == "O":
                dfs(i, j-1)
            if i < rows - 1 and board[i+1][j] == "O":
                dfs(i+1, j)
            if j < cols - 1 and board[i][j+1] == "O":
                dfs(i, j+1)

        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][cols-1] == "O":
                dfs(i, cols-1)

        for j in range(cols):
            if board[0][j] == "O":
                dfs(0, j)
            if board[rows-1][j] == "O":
                dfs(rows-1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "OO":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
