class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prods = collections.defaultdict(lambda:0)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                prods[nums[i] * nums[j]] += 1

        ans = 0
        for key, val in prods.items():
            ans += ((val * (val-1)) // 2) * 8

        return ans
