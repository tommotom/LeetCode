class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        ans = [1] * n

        if 1 not in nums: return ans

        children = defaultdict(list)
        for child, parent in enumerate(parents):
            children[parent].append(child)

        seen = [0] * 100010
        def dfs(i):
            if seen[nums[i]] == 0:
                for j in children[i]:
                    dfs(j)
                seen[nums[i]] = 1

        i = nums.index(1)
        miss = 1
        while i >= 0:
            dfs(i)
            while seen[miss] == 1:
                miss += 1
            ans[i] = miss
            i = parents[i]

        return ans
