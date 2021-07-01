from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        ans = 0
        for key, value in counter.items():
            if k - key in counter:
                if key != k - key:
                    tmp = min(value, counter[k - key])
                    counter[key] -= tmp
                    counter[k - key] -= tmp
                    ans += tmp
                else:
                    tmp = value // 2
                    counter[key] -= tmp * 2
                    ans += tmp
        return ans
