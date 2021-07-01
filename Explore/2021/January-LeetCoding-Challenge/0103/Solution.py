class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        def helper(position, leftnums):
            nonlocal ans
            if not leftnums:
                ans += 1
                return

            for num in leftnums:
                if num % position == 0 or position % num == 0:
                    helper(position + 1, leftnums - {num})

        helper(1, {i for i in range(1, n+1)})

        return ans
