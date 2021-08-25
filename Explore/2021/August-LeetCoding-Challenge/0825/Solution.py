class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        num_set = set()
        num = 0
        while pow(num, 2) <= c:
            num_set.add(pow(num, 2))
            if c- pow(num, 2) in num_set: return True
            num += 1
        return False
