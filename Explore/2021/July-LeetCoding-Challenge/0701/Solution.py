class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1: return [0, 1]
        tmp = self.grayCode(n-1)
        return tmp + [num + (2 << (n-2)) for num in reversed(tmp)]
