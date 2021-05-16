class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for i in range(2 ** len(nums)):
            tmp = 0
            b = 0
            while 2**b <= i:
                if (1 << b) & i:
                    tmp ^= nums[b]
                b += 1
            ans += tmp
        return ans
