class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        M = nums[-1]
        right = []
        for i in range(len(nums)-1, -1, -1):
            M = max(M, nums[i])
            right.append(M)
        right = right[::-1]

        M = nums[0]
        ans = 0
        for j in range(1, len(nums)-1):
            ans = max(ans, (M - nums[j]) * right[j+1])
            M = max(M, nums[j])

        return ans
