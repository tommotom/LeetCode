class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans, ans_set, length = [], set(), len(nums)

        def backtrack(used, path):
            nonlocal nums, ans, ans_set

            if all(used):
                if tuple(path) not in ans_set:
                    ans_set.add(tuple(path))
                    ans.append([i for i in path])
                return

            for i in range(length):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(used, path)
                    used[i] = False
                    path.pop()

        backtrack([False for _ in range(length)], [])
        return ans
