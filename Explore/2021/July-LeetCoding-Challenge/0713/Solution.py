class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l+1 < r:
            m = (l+r) // 2
            leftSide = nums[m-1] < nums[m] if m > 0 else True
            rightSide = nums[m] > nums[m+1] if m < len(nums) - 1 else True
            if leftSide & rightSide:
                return m
            elif leftSide:
                l = m
            else:
                r = m

        leftSide = nums[l-1] < nums[l] if l > 0 else True
        rightSide = nums[l] > nums[l+1] if l < len(nums) - 1 else True
        if leftSide and rightSide: return l
        return r
