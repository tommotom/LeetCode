class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = j = 0
        jmin = jmax = -1
        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                jmin, jmax, j = -1, -1, i+1
            if num == minK: jmin = i
            if num == maxK: jmax = i
            ans += max(0, min(jmin, jmax) - j + 1)

        return ans
