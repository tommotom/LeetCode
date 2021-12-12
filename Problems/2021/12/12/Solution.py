class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1 or sum(nums) % 2 == 1: return False

        target = sum(nums) // 2
        sums = set([0])

        for num in nums:
            next_sums = set()
            for s in sums:
                if s + num == target: return True
                elif s + num < target:
                    next_sums.add(s + num)
                if num < target:
                    next_sums.add(num)
                next_sums.add(s)
            sums = next_sums
        return False
