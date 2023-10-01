class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def number(count):
            if count < 2: return float('inf')
            if count == 2 or count == 3: return 1
            if count == 4: return 2
            if count == 5: return 2
            if count % 3 == 0: return count // 3
            if count % 3 == 1: return count // 3 + 1
            if count % 3 == 2: return count // 3 + 1

        c = Counter(nums)
        if any(float('inf') == number(count) for count in c.values()): return -1
        return sum(number(count) for count in c.values())
