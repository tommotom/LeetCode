class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        start = end = zeros = ans = 0
        while True:
            while end < n and (nums[end] == 1 or zeros < k):
                if nums[end] == 0: zeros += 1
                end += 1
            ans = max(ans, end - start)
            if end == n: break
            while start < n and zeros == k:
                if nums[start] == 0: zeros -= 1
                start += 1
        return ans
