class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        def liveNeighbors(i, j):
            nonlocal board, rows, cols
            lives = 0

            if i > 0:
                if j > 0: lives += board[i-1][j-1]
                lives += board[i-1][j]
                if j+1 < cols: lives += board[i-1][j+1]

            if j > 0: lives += board[i][j-1]
            if j+1 < cols: lives += board[i][j+1]

            if i+1 < rows:
                if j > 0: lives += board[i+1][j-1]
                lives += board[i+1][j]
                if j+1 < cols: lives += board[i+1][j+1]
            return lives

        ans = []
        for i in range(rows):
            row = []
            for j in range(cols):
                count = liveNeighbors(i, j)
                if board[i][j] == 1:
                    if count < 2 or count > 3: row.append(0)
                    else: row.append(1)
                else:
                    if count == 3: row.append(1)
                    else: row.append(0)
            ans.append(row)

        for i in range(rows):
            for j in range(cols):
                board[i][j] = ans[i][j]
