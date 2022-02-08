class Solution:
    def addDigits(self, num: int) -> int:
        return num if len(str(num)) == 1 else self.addDigits(sum(int(n) for n in str(num)))
