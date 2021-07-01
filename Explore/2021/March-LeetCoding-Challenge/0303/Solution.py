class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        for i in range(len(nums)):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans
