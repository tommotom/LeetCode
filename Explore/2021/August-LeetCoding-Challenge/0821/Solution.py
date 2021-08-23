class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        areas = [[set() for __ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                areas[i//3][j//3].add(board[i][j])

        def helper(i, j):
            nonlocal rows, cols, areas, board
            if i == 9: return True
            if j == 9: return helper(i+1, 0)

            if board[i][j] == ".":
                for num in range(1, 10):
                    str_num = str(num)
                    if isValid(i, j, str_num):
                        rows[i].add(str_num)
                        cols[j].add(str_num)
                        areas[i//3][j//3].add(str_num)
                        board[i][j] = str_num

                        if helper(i, j+1):
                            return True

                        rows[i].remove(str_num)
                        cols[j].remove(str_num)
                        areas[i//3][j//3].remove(str_num)
                        board[i][j] = "."
            else:
                return helper(i, j+1)

        def isValid(i, j, str_num):
            nonlocal rows, cols, areas
            return str_num not in rows[i] and str_num not in cols[j] and str_num not in areas[i//3][j//3]


        helper(0, 0)
        return board
