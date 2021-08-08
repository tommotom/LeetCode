class UnionFind:
    def __init__(self):
        self.uf = {}

    def find(self, u):
        if not u in self.uf:
            self.uf[u] = u
        if self.uf[u] == u: return u
        self.uf[u] = self.find(self.uf[u])
        return self.uf[u]

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        self.uf[u] = v

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])

        vals = defaultdict(list)
        for row in range(rows):
            for col in range(cols):
                vals[matrix[row][col]].append((row,col))

        cur_row = [0 for _ in range(rows)]
        cur_col = [0 for _ in range(cols)]
        ans = [[0] * cols for _ in range(rows)]
        for val in sorted(vals.keys()):
            uf = UnionFind()
            for row, col in vals[val]:
                uf.union(('row', row), ('col', col))
            groups = defaultdict(list)
            for row, col in vals[val]:
                groups[uf.find(('row', row))].append((row, col))
            for group in groups.values():
                rank = 0
                for row, col in group:
                    rank = max(cur_row[row], cur_col[col], rank)
                for row, col in group:
                    ans[row][col] = cur_row[row] = cur_col[col] = rank + 1
        return ans