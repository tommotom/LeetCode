class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            num_of_missing = arr[m] - (m + 1)
            if num_of_missing >= k:
                r = m
            else: l = m + 1

        if k <= num_of_missing:
            return arr[m] + (k - num_of_missing - 1)
        return arr[m] + (k - num_of_missing)
