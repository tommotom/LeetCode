class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cum = [nums[0]]
        for i in range(1, len(nums)):
            cum.append(cum[i-1]+nums[i])
        last = {}

        cur = 0
        ans = 0
        j = 0
        for i, num in enumerate(nums):
            if num in last:
                j = max(j, last[num])
                cur = cum[i] - cum[j]
            else:
                cur += num
            ans = max(ans, cur)
            last[num] = i
        return ans
