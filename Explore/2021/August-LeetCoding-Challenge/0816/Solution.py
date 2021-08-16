class NumArray:

    def __init__(self, nums: List[int]):
        self.cums = [0]
        for num in nums:
            self.cums.append(num + self.cums[-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.cums[right+1] - self.cums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)