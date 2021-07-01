class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return

        row, col = len(matrix), len(matrix[0])
        ans = []
        i = j = 0
        upright = True
        while True:
            ans.append(matrix[i][j])
            if i == row - 1 and j == col - 1: break

            if upright:
                if j == col - 1:
                    upright = False
                    i += 1
                elif i == 0:
                    upright = False
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == row - 1:
                    upright = True
                    j += 1
                elif j == 0:
                    upright = True
                    i += 1
                else:
                    i += 1
                    j -= 1

        return ans
