class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        b = format(n, 'b')[::-1]
        return [sum('1' == b[i] for i in range(0, len(b), 2)), sum('1' == b[i] for i in range(1, len(b), 2))]
