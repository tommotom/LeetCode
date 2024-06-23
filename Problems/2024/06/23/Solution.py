class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_heap, min_heap = [], []
        l, ans = -1, 0
        for i, num in enumerate(nums):
            while max_heap and -max_heap[0][0] - num > limit:
                l = max(heapq.heappop(max_heap)[1], l)
            while min_heap and num - min_heap[0][0] > limit:
                l = max(heapq.heappop(min_heap)[1], l)

            ans = max(ans, i - l)

            heapq.heappush(max_heap, (-num, i))
            heapq.heappush(min_heap, (num, i))

        return ans
