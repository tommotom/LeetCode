class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n

        length = [0] * n
        count = [1] * n

        for j, num_j in enumerate(nums):
            for i, num_i in enumerate(nums[:j]):
                if num_i < num_j:
                    if length[i] >= length[j]:
                        length[j] = length[i] + 1
                        count[j] = count[i]
                    elif length[i] + 1 == length[j]:
                        count[j] += count[i]

        maxLen = max(length)
        return sum(c for i, c in enumerate(count) if length[i] == maxLen)
