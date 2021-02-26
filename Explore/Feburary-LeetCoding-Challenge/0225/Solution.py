class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]
        left = 0
        for i in range(1, n):
            if prev > nums[i]:
                break
            if prev < nums[i]:
                prev = nums[i]
                left = i
        else:
            return 0

        prev = nums[-1]
        right = n-1
        for i in range(n-2, -1, -1):
            if prev < nums[i]:
                break
            if prev > nums[i]:
                prev = nums[i]
                right = i

        minNum = min(nums[left:right+1])
        maxNum = max(nums[left:right+1])

        lptr = 0
        while lptr < n:
            if nums[lptr] > minNum: break
            lptr += 1

        rptr = n-1
        while rptr >=0:
            if nums[rptr] < maxNum: break
            rptr -= 1

        return rptr - lptr + 1
