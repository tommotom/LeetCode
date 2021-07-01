class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-t for t in target]
        heapq.heapify(target)
        while True:
            num = -heapq.heappop(target)
            total -= num
            if num == 1 or total == 1: return True
            if num < total or total == 0 or num % total == 0:
                return False
            num %= total
            total += num
            heapq.heappush(target, -num)
