class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] *= 2

        mins = [min(nums)]
        maxs = list(map(lambda x: -x, nums))
        heapq.heapify(maxs)
        diff = -maxs[0] - mins[0]

        while maxs[0] % 2 == 0:
            num = heapq.heappop(maxs)
            num //= 2
            heapq.heappush(maxs, num)
            heapq.heappush(mins, -num)

            if -maxs[0] - mins[0] <= diff:
                diff = -maxs[0] - mins[0]

        return diff
