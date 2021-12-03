class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        for i in range(len(nums)):
            if nums[i] == 0:
                return max(0, self.maxProduct(nums[:i]), self.maxProduct(nums[i+1:]))

        minusCount = 0 if nums[0] > 0 else 1
        products = nums[0]
        for num in nums[1:]:
            if num < 0:
                minusCount += 1
            products *= num

        if minusCount % 2 == 0:
            return products

        left = right = products
        for num in nums:
            left //= num
            if num < 0:
                break

        for num in reversed(nums):
            right //= num
            if num < 0:
                break

        return max(left, right)
