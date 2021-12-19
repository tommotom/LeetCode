class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def LIS(nums):
            dp = [10**10] * (len(nums) + 1)
            for elem in nums: dp[bisect.bisect(dp, elem)] = elem
            return dp.index(10**10)

        ans = 0
        for i in range(k):
            tmp = arr[i::k]
            ans += len(tmp) - LIS(tmp)
        return ans
