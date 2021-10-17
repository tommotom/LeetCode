class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0
        for num in nums:
            target |= num

        def helper(idx, cur):
            nonlocal nums
            if idx == len(nums):
                if cur == 0: return 1
                return 0

            tmp = cur
            for i in range(17):
                if (1 << i) & cur and (1 << i) & nums[idx]:
                    tmp -= (1 << i)

            return helper(idx+1, cur) + helper(idx+1, tmp)

        return helper(0, target)
