class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        minimums = [float('inf')] * n
        for i in range(n-1, -1, -1):
            minimums[i] = min(minimums[i+1], nums[i]) if i < n-1 else nums[i]

        beauty = 0
        maximum = nums[0]
        for i in range(1, n-1):
            if maximum < nums[i] < minimums[i+1]:
                beauty += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                beauty += 1
            maximum = max(maximum, nums[i])
        return beauty
