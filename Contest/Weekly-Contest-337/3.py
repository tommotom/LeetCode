class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        def helper(i, arr):
            nonlocal ans
            if i == len(nums):
                ans += 1 if len(arr) > 0 else 0
                return

            if not nums[i] - k in arr:
                arr.append(nums[i])
                helper(i+1, arr)
                arr.pop()

            helper(i+1, arr)

        helper(0, [])

        return ans
