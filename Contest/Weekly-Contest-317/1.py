class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = c = 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                s += num
                c += 1

        return s // c if c > 0 else 0
