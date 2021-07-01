class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = [0 for _ in range(self.n)]
        self.arr = [0 for _ in range(self.n+1)]
        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        i = index + 1
        while i < len(self.arr):
            self.arr[i] += diff
            i += i & -i
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.sum(right+1) - self.sum(left)

    def sum(self, index):
        ret = 0
        while index > 0:
            ret += self.arr[index]
            index -= index & -index
        return ret


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)