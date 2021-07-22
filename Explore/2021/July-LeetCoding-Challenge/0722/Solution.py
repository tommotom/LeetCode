class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        mins = [float('inf') for _ in range(n)]
        maxs = [-float('inf') for _ in range(n)]
        for i in range(1, n):
            maxs[i] = max(maxs[i-1], nums[i-1])
        for i in range(n-2, -1, -1):
            mins[i] = min(mins[i+1], nums[i+1])
        for i in range(1,n):
            if maxs[i] <= mins[i-1]:
                return i
        return -1
