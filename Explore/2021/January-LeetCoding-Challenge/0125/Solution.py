class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = None
        for i, v in enumerate(nums):
            if v == 1:
                if last is not None and i - last <= k: return False
                last = i
        return True
