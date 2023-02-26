class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        leftSum, rightSum = [0], [0]
        for i in range(len(nums)-1):
            leftSum.append(leftSum[-1] + nums[i])
            rightSum.append(rightSum[-1] + nums[len(nums)-i-1])
        rightSum = rightSum[::-1]

        return [abs(leftSum[i] - rightSum[i]) for i in range(len(nums))]
