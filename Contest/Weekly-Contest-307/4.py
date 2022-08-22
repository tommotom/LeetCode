class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        abs_nums = sorted([abs(num) for num in nums])
        max_sum = sum([num for num in nums if num > 0])
        max_heap = [(-max_sum + abs_nums[0], 0)]
        ans = [max_sum]
        while len(ans) < k:
            next_sum, i = heapq.heappop(max_heap)
            heapq.heappush(ans, -next_sum)
            if i+1 < len(abs_nums):
                heapq.heappush(max_heap, (next_sum - abs_nums[i] + abs_nums[i+1], i+1))
                heapq.heappush(max_heap, (next_sum + abs_nums[i+1], i+1))

        return ans[0]
