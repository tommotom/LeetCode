class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        gcd = self.gcd(length, k)
        for i in range(gcd):
            tmp = nums[length - 1 - i]
            j = length - 1 - i
            while True:
                l = j - k
                if l < 0:
                    l = l + length
                if l == length - i - 1:
                    break
                nums[j] = nums[l]
                j = l
            nums[j] = tmp

    def gcd(self, a, b):
        if b == 0: return a
        return self.gcd(b, a % b)