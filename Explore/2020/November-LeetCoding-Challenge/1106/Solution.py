from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def divideSum(divisor):
            nonlocal nums
            ret = 0
            for num in nums:
                ret += ceil(num / divisor)
            return ret

        start = 1
        end = nums[-1]

        while start < end:
            mid = (start + end)//2
            result = divideSum(mid)
            if result > threshold:
                start = mid + 1
            else:
                end = mid

        return start
