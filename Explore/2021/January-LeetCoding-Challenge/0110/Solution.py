from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = SortedList()
        ans = 0
        for num in instructions:
            left = nums.bisect_left(num)
            right = nums.bisect_right(num)

            ans += min(left, len(nums) - right)
            ans %= 10**9 + 7
            nums.add(num)
        return ans
