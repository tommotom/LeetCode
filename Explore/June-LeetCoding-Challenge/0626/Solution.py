class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = []
        a = []
        for num in reversed(nums):
            a.append(bisect.bisect_left(s, num))
            bisect.insort(s, num)
        return reversed(a)
