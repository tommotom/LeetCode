class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == k: ans += 1
            for j in range(i+1, len(nums)):
                num = (num * nums[j]) // math.gcd(num, nums[j])
                if num == k: ans += 1

        return ans
