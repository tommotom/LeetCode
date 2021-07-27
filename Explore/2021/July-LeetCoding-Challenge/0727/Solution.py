class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if abs(target - tmp) < abs(diff):
                    diff = target - tmp
                if tmp < target:
                    l += 1
                else:
                    r -= 1
            if diff == 0:
                break
        return target - diff
