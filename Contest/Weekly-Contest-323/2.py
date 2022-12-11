class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        set_nums = set(nums)
        ans = -1
        visited = set()
        def dfs(num, streak):
            nonlocal visited, ans, set_nums
            ans = max(ans, streak)
            visited.add(num)
            sq = num * num
            if sq not in visited and sq in set_nums:
                dfs(sq, streak + 1)

        for num in nums:
            sq = num * num
            if sq not in visited and sq in set_nums:
                dfs(sq, 2)

        return ans
