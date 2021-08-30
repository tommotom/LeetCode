class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops == []:
            return m * n

        x = 0
        y = 0
        for i in ops:
            if x == 0:
                x = i[0]
            else:
                x = min(x, i[0])

            if y == 0:
                y = i[1]
            else:
                y = min(y, i[1])

        return x * y
