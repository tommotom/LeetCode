class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        ans = 0
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if dp[j][diff] > 0 :
                    ans += dp[j][diff]
                dp[i][diff] += dp[j][diff] + 1

        return ans
