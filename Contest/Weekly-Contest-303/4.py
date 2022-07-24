class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:

        def hamming(num):
            ret = 0
            for b in range(0, 32):
                if (1<<b) & num: ret += 1
            return ret

        weights = [hamming(num) for num in set(nums)]
        weights.sort()

        ans = 0
        for h in weights:
            ans += len(weights) - bisect.bisect_left(weights, k-h)
        return ans
