class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] > threshold: continue
            if nums[i] % 2 == 0:
                length = 1
                for j in range(i+1, len(nums)):
                    if nums[j] > threshold: break
                    if nums[j] % 2 == nums[j-1] % 2: break
                    length += 1
                ans = max(ans, length)
        return ans
