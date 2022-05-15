class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_num = max(candidates)
        max_digit = 0
        while max_num > (1 << max_digit):
            max_digit += 1

        ans = 0
        for d in range(max_digit+1):
            count = 0
            bit = 1 << d
            for can in candidates:
                if can & bit:
                    count += 1
            ans = max(ans, count)
        return ans
