class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reached = 0
        for i, num in enumerate(nums):
            if reached < i: return False
            reached = max(reached, i + num)
        return True
