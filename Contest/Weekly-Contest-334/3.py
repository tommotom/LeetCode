class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        ans = 0
        picked = set()
        for j in range(len(nums)//2, len(nums)):
            if 2 * nums[i] <= nums[j]:
                if i not in picked:
                    ans += 2
                picked.add(i)
                picked.add(j)
                i += 1

        return ans
