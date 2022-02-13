class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0

        even = Counter(nums[::2])
        odd = Counter(nums[1::2])

        even_heap = []
        for k, v in even.items():
            heapq.heappush(even_heap, (-v, k))

        odd_heap = []
        for k, v in odd.items():
            heapq.heappush(odd_heap, (-v, k))

        ec, ek = heapq.heappop(even_heap)
        ec *= -1
        oc, ok = heapq.heappop(odd_heap)
        oc *= -1

        if ek == ok:
            if even_heap and odd_heap:
                if ec + even_heap[0][0] > oc + odd_heap[0][0]:
                    oc, ok = heapq.heappop(odd_heap)
                    oc *= -1
                else:
                    ec, ek = heapq.heappop(even_heap)
                    ec *= -1
            elif even_heap:
                ec, ek = heapq.heappop(even_heap)
                ec *= -1
            elif odd_heap:
                oc, ok = heapq.heappop(odd_heap)
                oc *= -1
            else:
                oc, ok = 0, 0

        return len(nums) - ec - oc
