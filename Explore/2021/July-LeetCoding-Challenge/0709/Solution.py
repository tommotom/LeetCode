class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n, m = len(nums), max(nums)
        length_to_min = [float('inf') for _ in range(n)]
        ans = 1
        for i, num in enumerate(nums):
            length_to_min[0] = min(length_to_min[0], num)
            l, r = 0, n-1
            while l+1 < r:
                m = (l+r) // 2
                if length_to_min[m] < num:
                    l = m
                else:
                    r = m
            if length_to_min[r] < num:
                length_to_min[r+1] = min(length_to_min[r+1], num)
                ans = max(ans, r+2)
            elif length_to_min[l] < num:
                length_to_min[l+1] = min(length_to_min[l+1], num)
                ans = max(ans, l+2)
        return ans
