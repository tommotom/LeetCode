class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        isDivisible = [True if num % p == 0 else False for num in nums]
        cum = [0]
        for i in range(len(isDivisible)):
            if isDivisible[i]:
                cum.append(cum[-1]+1)
            else:
                cum.append(cum[-1])
        ans = 0
        visited = set()
        for i in range(1, len(cum)):
            for j in range(i):
                if cum[i] - cum[j] <= k and tuple(nums[j:i]) not in visited:
                    ans += 1
                    visited.add(tuple(nums[j:i]))

        return ans
