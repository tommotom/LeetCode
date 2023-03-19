class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counter = Counter(map(lambda x: x%value, nums))
        for i in range(value):
            if i not in counter: counter[i] = 0

        m = min(counter.values())
        for i in range(value):
            if counter[i] == m:
                return value * (counter[i]) + i
