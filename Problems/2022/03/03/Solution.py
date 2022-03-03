class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+2, len(nums)):
                if not nums[j] - nums[j-1] == diff: break
                ans += 1
        return ans
