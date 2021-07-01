class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0] or matrix[0][0] > target: return False

        left, right = 0, len(matrix[0])

        while left < right:
            mid = (left + right) // 2
            if matrix[0][mid] < target: left = mid + 1
            else: right = mid

        if left < len(matrix[0]) and matrix[0][left] == target: return True

        return self.searchMatrix(matrix[1:], target)
