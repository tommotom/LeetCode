class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for bit in range(pow(2, len(nums))):
            arr = []
            for i in range(len(nums)):
                if bit & (1 << i) > 0:
                    arr.append(nums[i])
            ans.append(arr)
        return ans
