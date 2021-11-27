class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = 1

        if 0 in nums and Counter(nums)[0] == 1:
            idx = nums.index(0)
            for i, num in enumerate(nums):
                if i == idx:
                    continue
                products *= num
            return [0 if num != 0 else products for num in nums]

        for num in nums:
            products *= num
        return [products//num if num != 0 else products for num in nums]
