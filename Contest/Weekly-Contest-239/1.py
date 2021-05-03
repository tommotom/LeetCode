class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if nums[start] == target: return 0
        l, r = start - 1, start + 1
        while 0 <= l and r < len(nums):
            if nums[l] == target: return start-l
            if nums[r] == target: return r-start
            l -= 1
            r += 1
        while 0 <= l:
            if nums[l] == target: return start-l
            l -= 1
        while r < len(nums):
            if nums[r] == target: return r-start
            r += 1
        return -1
