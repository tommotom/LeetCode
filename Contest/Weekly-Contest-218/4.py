class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        d = len(nums) // k

        @lru_cache(None)
        def helper(nums):
            if not nums:
                return 0
            ret = 10 ** 15
            for a in combinations(nums, d):
                if len(set(a)) < d: continue
                left = list(nums)
                for v in a:
                    left.remove(v)
                ret = min(ret, max(a) - min(a) + helper(tuple(left)))
            return ret

        ans = helper(tuple(nums))
        return ans if ans != 10 ** 15 else -1
