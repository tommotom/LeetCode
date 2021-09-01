class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            count = 0
            i = num
            while nums[i] >= 0:
                tmp = i
                i = nums[i]
                nums[tmp] = -1
                count += 1
            ans = max(ans, count)
        return ans
