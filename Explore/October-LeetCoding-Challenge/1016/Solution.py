class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False

        start, end = 0, len(matrix)
        while start < end:
            mid = (start + end) // 2
            if matrix[mid][-1] < target:
                start = mid + 1
            else:
                end = mid
        row = start

        if row == len(matrix): return False

        start, end = 0, len(matrix[row])
        while start < end:
            mid = (start + end) // 2
            if matrix[row][mid] < target:
                start = mid + 1
            else:
                end = mid

        return matrix[row][start] == target
