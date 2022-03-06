class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        def sumOf(begin, end):
            n = end - begin + 1
            return (n * (n+1)) // 2

        sumOfUnders = 0
        for num in sorted(list(set(nums))):
            if num <= k:
                k += 1
                sumOfUnders += num

        return sumOf(1, k) - sumOfUnders
