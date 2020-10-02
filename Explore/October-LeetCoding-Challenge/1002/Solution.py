class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        length, ans = len(candidates), []
        candidates.sort()

        def backtrack(idx, val, comb):
            nonlocal length, ans, candidates, target
            if val == 0:
                ans.append([i for i in comb])
                return

            if idx == length or candidates[idx] > val: return

            for i in range(idx, length):
                comb.append(candidates[i])
                backtrack(i, val-candidates[i], comb)
                comb.pop()

            return

        backtrack(0, target, [])
        return ans
