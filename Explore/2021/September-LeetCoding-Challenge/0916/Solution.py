class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        visited_count = 0
        VISITED = 101
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        current = 0

        i, j = 0, 0
        ans = []
        while True:
            ans.append(matrix[i][j])
            matrix[i][j] = VISITED
            visited_count += 1

            if visited_count == row * col: break

            next_i, next_j = i + direction[current][0], j + direction[current][1]
            while not 0 <= next_i < row or not 0 <= next_j < col or matrix[next_i][next_j] == VISITED:
                current = (current + 1) % 4
                next_i, next_j = i + direction[current][0], j + direction[current][1]
            i, j = next_i, next_j
        return ans
