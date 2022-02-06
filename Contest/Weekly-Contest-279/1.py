class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = sorted(nums[1::2], reverse=True)
        even = sorted(nums[::2])

        ans = []
        for i in range(len(even)):
            ans.append(even[i])
            if i < len(odd):
                ans.append(odd[i])
        return ans
