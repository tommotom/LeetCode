class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def canConstractWord(i, j, k, visited):
            nonlocal board, word, m, n
            visited.add((i, j))
            if k == len(word): return True
            if i > 0 and (i-1, j) not in visited and board[i-1][j] == word[k] and canConstractWord(i-1, j, k+1, visited): return True
            if j > 0 and (i, j-1) not in visited and board[i][j-1] == word[k] and canConstractWord(i, j-1, k+1, visited): return True
            if i < m-1 and (i+1, j) not in visited and board[i+1][j] == word[k] and canConstractWord(i+1, j, k+1, visited): return True
            if j < n-1 and (i, j+1) not in visited and board[i][j+1] == word[k] and canConstractWord(i, j+1, k+1, visited): return True
            visited.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if canConstractWord(i, j, 1, set()):
                        return True
        return False
