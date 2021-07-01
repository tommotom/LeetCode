class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k, i = -1, len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                k = i
                break
            i -= 1

        if k == -1:
            nums.sort()
            return

        l = len(nums) - 1
        while l > k:
            if nums[k] < nums[l]: break
            l -= 1

        nums[k], nums[l] = nums[l], nums[k]

        nums[k+1:] = reversed(nums[k+1:])

        return
