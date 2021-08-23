class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxNum = max(nums)
        minNum = min(nums)
        for num in range(maxNum, 0, -1):
            if maxNum % num == 0 and minNum % num == 0:
                return num
