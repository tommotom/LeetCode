class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        pre = defaultdict(int)
        suf = Counter(nums)
        ret = []
        for num in nums:
            pre[num] += 1
            suf[num] -= 1
            if suf[num] == 0:
                del suf[num]
            ret.append(len(pre) - len(suf))
        return ret
