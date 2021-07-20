class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.shuffled = [num for num in nums]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        return self.nextPerm()

    def nextPerm(self):
        k = -1
        i = len(self.shuffled) - 2
        while i >= 0:
            if self.shuffled[i] < self.shuffled[i+1]:
                k = i
                break
            i -= 1

        if k == -1:
            self.shuffled.reverse()
            return self.shuffled

        l = k + 1
        i = len(self.shuffled) - 1
        while i > k+1:
            if self.shuffled[k] < self.shuffled[i]:
                l = i
                break
            i -= 1

        tmp = self.shuffled[k]
        self.shuffled[k] = self.shuffled[l]
        self.shuffled[l] = tmp

        self.shuffled[k+1:] = reversed(self.shuffled[k+1:])

        return self.shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
