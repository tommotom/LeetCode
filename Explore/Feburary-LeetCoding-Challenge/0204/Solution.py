from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        vals = sorted(list(set(nums)))
        ans = 0
        for i in range(len(vals)-1):
            if vals[i+1] - vals[i] == 1:
                ans = max(ans, counter[vals[i]] + counter[vals[i+1]])
        return ans
