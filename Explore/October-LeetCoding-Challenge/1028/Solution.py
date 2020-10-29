class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if not nums: return ans
        first = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] + 1 != nums[i]:
                if first == nums[i-1]:
                    ans.append(str(first))
                else:
                    ans.append(str(first)+"->"+str(nums[i-1]))
                first = nums[i]
        if first == nums[-1]:
            ans.append(str(first))
        else:
            ans.append(str(first)+"->"+str(nums[-1]))

        return ans
