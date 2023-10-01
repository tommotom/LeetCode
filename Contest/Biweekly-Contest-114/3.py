class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        score = nums[0]
        for num in nums[1:]:
            score &= num

        cum = [nums[0]]
        for num in nums[1:]:
            cum.append(cum[-1] & num)

        cur = nums[-1]
        ans = 1
        for i in range(len(nums)-2, -1, -1):
            if cur + cum[i] == score:
                ans += 1
                score -= cur
                cur = nums[i]
            cur &= nums[i]

        return ans
