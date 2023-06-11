class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        m, M = nums[0], nums[-1]
        for num in nums:
            if num != m and num != M:
                return num
        return -1
