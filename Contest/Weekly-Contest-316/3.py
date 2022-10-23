class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def calc(x):
            ret = 0
            for num, c in zip(nums, cost):
                ret += abs(num - x) * c
            return ret

        low, high = min(nums), max(nums)
        while ((high - low) > 2):
            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3

            cost1 = calc(mid1)
            cost2 = calc(mid2)

            if (cost1 < cost2):
                high = mid2
            else:
                low = mid1


        return min(calc((low + high)//2), calc((low + high)//2 + 1))
