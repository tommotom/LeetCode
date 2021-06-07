class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        largests = ans = 0
        for largest in sorted(counter.keys(), reverse=True):
            ans += largests
            largests += counter[largest]
        return ans
