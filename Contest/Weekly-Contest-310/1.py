class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            if num % 2 == 0: counter[num] += 1

        fre_to_nums = defaultdict(list)
        m = 0
        for k, v in counter.items():
            m = max(m, v)
            fre_to_nums[v].append(k)
        if not fre_to_nums: return -1
        return sorted(fre_to_nums[m])[0]
