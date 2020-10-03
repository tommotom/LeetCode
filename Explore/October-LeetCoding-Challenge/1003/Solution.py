from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            ans, nums = 0, Counter(nums)
            for num, count in nums.items():
                if count > 1: ans += 1
        else:
            ans, nums = 0, set(nums)
            while nums:
                num = nums.pop()
                if num-k in nums: ans += 1
                if num+k in nums: ans += 1

        return ans
