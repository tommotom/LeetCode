class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return[]

        ans = []
        consecutive = None
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                if not consecutive:
                    consecutive = [str(nums[i]), str(nums[i+1])]
                else:
                    consecutive[1] = str(nums[i+1])
            else:
                if consecutive:
                    ans.append("->".join(consecutive))
                    consecutive = None
                else:
                    ans.append(str(nums[i]))
        if consecutive:
            ans.append("->".join(consecutive))
        else:
            ans.append(str(nums[-1]))

        return ans
