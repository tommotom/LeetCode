class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        max_array = [None] * (len(nums)-2) + [nums[-1]]
        for i in range(len(nums)-3, -1, -1):
            max_array[i] = max(max_array[i+1], nums[i+1])

        min_num = nums[0]
        for i in range(1, len(nums)-1):
            if min_num < nums[i] < max_array[i-1]: return True
            min_num = min(min_num, nums[i])

        return False
