class UF:
    def __init__(self, row, col):
        self.parent = {}
        self.parent["start"] = "start"
        self.parent["end"] = "end"
        for r in range(row):
            for c in range(col):
                self.parent[(r, c)] = (r, c)

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q: return
        self.parent[root_p] = root_q

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        arr = [[0] * col for _ in range(row)]
        for r, c in cells:
            arr[r-1][c-1] = 1

        uf = UF(row, col)
        for r in range(row):
            for c in range(col):
                if arr[r][c] == 0:
                    if r == 0:
                        uf.union("start", (r, c))
                    if r > 0 and arr[r-1][c] == 0:
                        uf.union((r-1, c), (r, c))
                    if c > 0 and arr[r][c-1] == 0:
                        uf.union((r, c-1), (r, c))
                    if r+1 < row and arr[r+1][c] == 0:
                        uf.union((r+1, c), (r, c))
                    if c+1 < col and arr[r][c+1] == 0:
                        uf.union((r, c+1), (r, c))
                    if r == row-1:
                        uf.union("end", (r,c))

        day = len(cells)
        while uf.find("start") != uf.find("end"):
            day -= 1
            r, c = cells[day]
            r -= 1
            c -= 1
            arr[r][c] = 0
            if r == 0:
                uf.union("start", (r, c))
            if r > 0 and arr[r-1][c] == 0:
                uf.union((r-1, c), (r, c))
            if c > 0 and arr[r][c-1] == 0:
                uf.union((r, c-1), (r, c))
            if r+1 < row and arr[r+1][c] == 0:
                uf.union((r+1, c), (r, c))
            if c+1 < col and arr[r][c+1] == 0:
                uf.union((r, c+1), (r, c))
            if r == row-1:
                uf.union("end", (r,c))
        return day
