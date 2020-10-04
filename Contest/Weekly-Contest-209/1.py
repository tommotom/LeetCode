from collections import Counter

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        counter = Counter(nums)
        total = len(nums)
        for i in range(max(nums)+1):
            if i == total: return i
            if i in counter: total -= counter[i]
        return -1
