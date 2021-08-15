class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        half = len(nums)//2
        for i in range(half):
            ans.append(nums[i+half])
            ans.append(nums[i])
        if len(nums) % 2 == 1:
            ans.append(nums[-1])
        return ans
