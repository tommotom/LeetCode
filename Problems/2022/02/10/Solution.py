class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        ans = cum = 0
        for num in nums:
            cum += num
            if cum == k: ans += 1
            ans += counter[cum-k]
            counter[cum] += 1

        return ans
