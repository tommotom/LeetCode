class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0: return 0
        if num1 >= num2: return self.countOperations(num1-num2, num2) + 1
        else: return self.countOperations(num1, num2-num1) + 1
