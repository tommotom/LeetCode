class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        total = 0
        for i in range(k):
            counter[nums[i]] += 1
            total += nums[i]

        ans = total if len(counter) == k else 0
        for i in range(k, len(nums)):
            counter[nums[i-k]] -= 1
            total -= nums[i-k]
            if counter[nums[i-k]] == 0:
                del counter[nums[i-k]]

            counter[nums[i]] += 1
            total += nums[i]
            if len(counter) == k:
                ans = max(ans, total)

        return ans
