class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        aXORb = 0
        for num in nums:
            aXORb ^= num

        rightMost = aXORb & (-aXORb)
        a = 0
        for num in nums:
            if rightMost & num:
                a ^= num

        return [a, aXORb ^ a]
