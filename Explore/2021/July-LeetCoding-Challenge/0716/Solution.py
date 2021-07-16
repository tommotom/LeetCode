class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n, twoSums = len(nums), defaultdict(list)

        for i in range(n-1):
            for j in range(i+1, n):
                twoSums[nums[i]+nums[j]].append((i, j))

        ans = []
        visited = set()
        for s in twoSums:
            rest = target - s
            if not rest in twoSums: continue
            for a, b in twoSums[s]:
                for c, d in twoSums[rest]:
                    if a == c or a == d or b == c or b == d: continue
                    val = sorted([nums[a], nums[b], nums[c], nums[d]])
                    tup = tuple(val)
                    if tup in visited: continue
                    ans.append(val)
                    visited.add(tup)
        return ans
