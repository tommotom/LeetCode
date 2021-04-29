class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1,-1]

        l, r = 0, len(nums)
        while l < r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        if not l < len(nums) or nums[l] != target: return[-1,-1]

        start = l

        l, r = 0, len(nums)
        while l < r:
            m = (l+r) // 2
            if nums[m] < target+1:
                l = m + 1
            else:
                r = m

        return [start, l-1]
