class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        negs = set()
        for num in nums:
            if num < 0: negs.add(num)

        ans = -1
        for num in nums:
            if num > 0 and num > ans and -num in negs:
                ans = num
        return ans
