class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        dp = []
        for i, num in enumerate(nums):
            divisors = set([num])
            for j in range(i):
                if num % nums[j] == 0 and len(dp[j])+1 > len(divisors):
                    divisors = copy.copy(dp[j])
                    divisors.add(num)
            dp.append(divisors)

        idx, length = 0, 1
        for i in range(len(dp)):
            if length < len(dp[i]):
                length = len(dp[i])
                idx = i

        return list(dp[idx])
