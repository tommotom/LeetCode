class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        count_to_idx = {0:-1}
        ans = 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in count_to_idx:
                ans = max(ans, i - count_to_idx[count])
            else:
                count_to_idx[count] = i
        return ans
