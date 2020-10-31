from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = sorted(Counter(nums).items(), key=lambda x: (x[1], x[0]))
        ans = []
        for num, count in counter.items():
            ans += [num] * count
        return ans
