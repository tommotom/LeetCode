class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = neg = 0
        while nums[pos] < 0: pos += 1
        while nums[neg] > 0: neg += 1

        ans = []
        while pos < len(nums):
            ans.append(nums[pos])
            pos += 1
            while pos < len(nums) and nums[pos] < 0: pos += 1

            ans.append(nums[neg])
            neg += 1
            while neg < len(nums) and nums[neg] > 0: neg += 1

        return ans
