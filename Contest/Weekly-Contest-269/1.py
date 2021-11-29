class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i, num in enumerate(sorted(nums)):
            if num == target:
                ans.append(i)
        return ans
