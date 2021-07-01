class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0] * i for i in range(1, 102)]
        tower[0][0] = poured

        for i in range(len(tower)-1):
            should_next_row = False
            for j in range(len(tower[i])):
                if tower[i][j] > 1.0:
                    excess = tower[i][j] - 1.0
                    tower[i][j] = 1.0
                    tower[i+1][j] += excess/2
                    tower[i+1][j+1] += excess/2
                    should_next_row = True
            if not should_next_row: break

        return tower[query_row][query_glass]
