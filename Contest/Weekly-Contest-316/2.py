class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            n = nums[i]
            for j in range(i, -1, -1):
                n = math.gcd(n, nums[j])
                if n == k: ans += 1
        return ans
