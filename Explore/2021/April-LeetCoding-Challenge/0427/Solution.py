class Solution:
    SET = set([3**x for x in range(20)])
    def isPowerOfThree(self, n: int) -> bool:
        return n in (self.SET)
