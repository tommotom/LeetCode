class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        ans = []
        nums.sort()
        for bit in range(pow(2, len(nums))):
            tmp = []
            for i in range(len(nums)):
                if (1 << i) & bit:
                    tmp.append(nums[i])
            if tuple(tmp) not in visited:
                visited.add(tuple(tmp))
                ans.append(tmp)
        return ans
