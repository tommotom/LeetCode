class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(num):
            ret = 0
            while num > 0:
                ret *= 10
                ret += num % 10
                num //= 10
            return ret

        return len(set(nums) | {reverse(num) for num in nums})
