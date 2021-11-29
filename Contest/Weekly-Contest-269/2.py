class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        elements = 2 * k + 1
        ans = [-1 for _ in range(len(nums))]
        total = sum(nums[:min(len(nums),elements)])
        for i in range(k, max(len(nums)-k, 0)):
            ans[i] = total // elements
            if i+k+1 < len(nums):
                total += nums[i+k+1]
            total -= nums[i-k]
        return ans
