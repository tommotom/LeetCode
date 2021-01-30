class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 1: nums[i] *= 2
            nums[i] *= -1

        nums = sorted(list(set(nums)))

        if len(nums) == 1: return 0

        max_val, min_val = nums.pop(0), nums[-1]

        ans = max_val - min_val

        heapq.heapify(nums)

        while max_val % 2 == 0:
            max_val //= 2
            min_val = max(min_val, max_val)
            if nums and max_val == nums[0]: max_val = heapq.heappop(nums)
            elif nums and max_val > nums[0]:
                heapq.heappush(nums, max_val)
                max_val = heapq.heappop(nums)
            ans = max(ans, max_val - min_val)

        return ans * -1