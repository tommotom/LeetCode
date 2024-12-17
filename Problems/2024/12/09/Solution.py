class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        bad = []
        for i in range(len(nums)-1):
            if nums[i] % 2 == nums[i+1] % 2:
                bad.append((i, i+1))

        if not bad: return [True] * len(queries)

        ans = []

        for s, e in queries:
            l, r = 0, len(bad)
            while l < r:
                m = l + (r - l) // 2
                if bad[m][0] < s:
                    l = m + 1
                else:
                    r = m
            if l < len(bad) and s <= bad[l][0] and bad[l][1] <= e:
                ans.append(False)
            else:
                ans.append(True)

        return ans
