class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def helper(i, arr, target):
            nonlocal ans
            if target == 0:
                ans.append(list(arr))
                return
            if i < 0: return

            count = 0
            while candidates[i] <= target:
                count += 1
                arr.append(candidates[i])
                target -= candidates[i]
                helper(i-1, arr, target)
            for _ in range(count):
                target += arr.pop()

            helper(i-1, arr, target)

        helper(len(candidates)-1, [], target)

        return ans
