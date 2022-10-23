class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        def helper(nums, target):
            return sum(abs(num - t) // 2 for num, t in zip(nums, target))

        nums.sort()
        target.sort()

        odd_nums = [num for num in nums if num % 2 == 1]
        odd_target = [num for num in target if num % 2 == 1]
        even_nums = [num for num in nums if num % 2 == 0]
        even_target = [num for num in target if num % 2 == 0]

        return (helper(odd_nums, odd_target) + helper(even_nums, even_target)) // 2
