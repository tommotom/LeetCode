class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        maxs, mins = [], []
        for i in range(len(nums)):
            maxs.append([nums[i]])
            mins.append([nums[i]])
            for j in range(i+1, len(nums)):
                maxs[i].append(max(maxs[i][-1], nums[j]))
                mins[i].append(min(mins[i][-1], nums[j]))

        ans = 0
        for i in range(len(maxs)):
            for j in range(len(maxs[i])):
                ans += maxs[i][j] - mins[i][j]

        return ans
