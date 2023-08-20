class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)

        ans = 0
        for num, arr in indices.items():
            l = deleted = 0
            for r in range(len(arr)):
                deleted += 0 if r == 0 else arr[r] - arr[r-1] - 1
                while deleted > k:
                    deleted -= arr[l+1] - arr[l] - 1
                    l += 1
                ans = max(ans, r - l + 1)

        return ans
