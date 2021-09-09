class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        row_mines, col_mines = [[] for _ in range(n)], [[] for _ in range(n)]
        for r, c in mines:
            bisect.insort(row_mines[r], c)
            bisect.insort(col_mines[c], r)

        l, h = -1, math.ceil(n/2)
        ans = 0
        while l < h:
            length = math.ceil((l+h) / 2)
            valid = False
            for r in range(length-1, n-length+1):
                if valid: break
                for c in range(length-1, n-length+1):
                    if row_mines[r] and bisect.bisect_left(row_mines[r], c-length+1) != bisect.bisect(row_mines[r], c+length-1): continue
                    if col_mines[c] and bisect.bisect_left(col_mines[c], r-length+1) != bisect.bisect(col_mines[c], r+length-1): continue
                    valid = True
                    break
            if valid:
                l = length
                ans = max(ans, length)
            else:
                h = length - 1
        return ans
