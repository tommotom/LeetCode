class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.cum = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.cum[i+1][j+1] = self.cum[i+1][j] + self.cum[i][j+1] - self.cum[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cum[row2+1][col2+1] - self.cum[row2+1][col1] - self.cum[row1][col2+1] + self.cum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)