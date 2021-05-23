class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def helper(nums, index, path, ans):
            if index == len(nums):
                ans.append(path)
                return
            for i in range(len(nums)):
                nums[index] = i
                if isValid(nums, index):
                    tmp = "." * len(nums)
                    helper(nums, index+1, path+[tmp[:i]+"Q"+tmp[i+1:]], ans)

        def isValid(nums, n):
            for i in range(n):
                if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]: return False
            return True

        helper([-1]*n, 0, [], ans)
        return ans
