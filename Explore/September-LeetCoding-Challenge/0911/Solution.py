class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1: return nums[0]

        first, last, cum = 1, 1, 1
        for i in range(length):
            if nums[i] == 0:
                tmp = [0]
                if i > 0: tmp.append(self.maxProduct(nums[:i]))
                if i + 1 < length: tmp.append(self.maxProduct(nums[i+1:]))
                return max(tmp)
            elif nums[i] < 0:
                if first == 1: first = cum * nums[i]
                last = cum
            cum *= nums[i]

        return max(cum, cum // first, last)
