class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            seen = set()
            cur = -1
            for j in range(i, n):
                cur += 0 if nums[j] in seen else 1 - (nums[j] + 1 in seen) - (nums[j] - 1 in seen)
                ans += cur
                seen.add(nums[j])
        return ans
