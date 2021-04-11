class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        minus = 0
        for x in nums:
            if x < 0: minus += 1
        if minus % 2 == 0: return 1
        return -1
