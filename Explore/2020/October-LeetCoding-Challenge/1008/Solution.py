class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1

        start, end = 0, len(nums)-1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        mid = (start + end) // 2
        if nums[mid] == target: return mid
        return -1
